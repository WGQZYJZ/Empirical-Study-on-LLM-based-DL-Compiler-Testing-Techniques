'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
torch.Tensor.pow(input_tensor, 2)
print(input_tensor)
torch.pow(input_tensor, 2)
print(input_tensor)
torch.pow(input_tensor, 2, out=input_tensor)
print(input_tensor)
torch.pow(input_tensor, 2, out=input_tensor)
print(input_tensor)
torch.pow