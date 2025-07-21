'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_tensor = torch.rand(1, 3, 224, 224)
torch.Tensor.new_ones(input_tensor, (1, 3, 224, 224))