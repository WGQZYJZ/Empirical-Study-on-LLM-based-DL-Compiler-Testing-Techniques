'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagflat\ntorch.Tensor.diagflat(_input_tensor, offset=0)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor.diagflat(offset=0))