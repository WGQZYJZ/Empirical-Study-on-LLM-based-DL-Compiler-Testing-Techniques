'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igammac\ntorch.Tensor.igammac(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4, dtype=torch.float)
other = torch.randn(4, 4, dtype=torch.float)
print(torch.Tensor.igammac(input_tensor, other))