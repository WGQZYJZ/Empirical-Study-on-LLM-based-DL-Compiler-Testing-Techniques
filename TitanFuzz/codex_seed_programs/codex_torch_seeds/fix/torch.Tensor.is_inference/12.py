'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_inference\ntorch.Tensor.is_inference(_input_tensor)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
_input_tensor = torch.randn(1, 3, 224, 224)
torch.Tensor.is_inference(_input_tensor)