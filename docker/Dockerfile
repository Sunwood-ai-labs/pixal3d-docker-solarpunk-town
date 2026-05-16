FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    CUDA_HOME=/usr/local/cuda \
    TORCH_CUDA_ARCH_LIST="8.6;8.9" \
    OPENCV_IO_ENABLE_OPENEXR=1 \
    PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
    ATTN_BACKEND=flash_attn

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash build-essential ca-certificates curl git libgl1 libglib2.0-0 \
    libjpeg-dev ninja-build wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash /tmp/miniconda.sh -b -p /opt/conda \
    && rm /tmp/miniconda.sh

ENV PATH=/opt/conda/bin:$PATH

RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main \
    && conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

RUN conda install -y python=3.10 pip && conda clean -afy

RUN pip install torch==2.6.0 torchvision==0.21.0 --index-url https://download.pytorch.org/whl/cu124

WORKDIR /workspace

RUN git clone --depth 1 https://github.com/microsoft/TRELLIS.2.git /workspace/TRELLIS.2

COPY . /workspace/Pixal3D

WORKDIR /workspace/TRELLIS.2

RUN pip install imageio imageio-ffmpeg tqdm easydict opencv-python-headless ninja \
    trimesh transformers gradio==6.0.1 tensorboard pandas lpips zstandard kornia timm \
    diffusers==0.37.1 accelerate==1.13.0 plyfile==1.1.3 rembg onnxruntime-gpu \
    git+https://github.com/microsoft/MoGe.git

# TRELLIS.2 CUDA/C++ extensions.
RUN pip install flash-attn==2.7.3 --no-build-isolation
RUN git clone -b v0.4.0 https://github.com/NVlabs/nvdiffrast.git /tmp/nvdiffrast \
    && pip install /tmp/nvdiffrast --no-build-isolation
RUN git clone -b renderutils https://github.com/JeffreyXiang/nvdiffrec.git /tmp/nvdiffrec \
    && pip install /tmp/nvdiffrec --no-build-isolation
RUN git clone --recursive https://github.com/JeffreyXiang/CuMesh.git /tmp/CuMesh \
    && pip install /tmp/CuMesh --no-build-isolation
RUN git clone --recursive https://github.com/JeffreyXiang/FlexGEMM.git /tmp/FlexGEMM \
    && pip install /tmp/FlexGEMM --no-build-isolation
RUN pip install /workspace/TRELLIS.2/o-voxel --no-build-isolation

WORKDIR /workspace/Pixal3D

RUN pip install -r requirements.txt --no-build-isolation \
    && pip install --force-reinstall "natten==0.17.5+torch260cu124" -f https://whl.natten.org --no-deps \
    && pip install https://github.com/LDYang694/Storages/releases/download/20260430/utils3d-0.0.2-py3-none-any.whl

ENV PYTHONPATH=/workspace/Pixal3D:/workspace/TRELLIS.2:$PYTHONPATH

EXPOSE 7860

CMD ["python", "inference.py", "--image", "assets/images/0_img.png", "--output", "/workspace/Pixal3D/outputs/output.glb", "--fov", "0.2"]
