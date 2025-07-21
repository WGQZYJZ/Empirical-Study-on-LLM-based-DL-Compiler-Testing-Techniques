'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print(torch.Tensor.digamma(input_tensor))