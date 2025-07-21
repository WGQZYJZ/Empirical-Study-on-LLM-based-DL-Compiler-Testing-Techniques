'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma\ntorch.Tensor.lgamma(_input_tensor)\n'
import torch
input_data = torch.randn(3, 4)
res = torch.Tensor.lgamma(input_data)
print(res)