'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma\ntorch.Tensor.mvlgamma(_input_tensor, p)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor.mvlgamma(3))
print(input_tensor.mvlgamma(5))