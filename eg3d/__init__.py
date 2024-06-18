import sys
from eg3d import torch_utils,training, dnnlib

sys.modules["torch_utils"] = torch_utils
sys.modules["training"] = training
sys.modules["dnnlib"] = dnnlib