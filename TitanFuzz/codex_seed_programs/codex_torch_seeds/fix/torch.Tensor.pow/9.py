'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
input_tensor = torch.randn(3, 3)
pow_tensor = input_tensor.pow(2)
print(pow_tensor)
pow_tensor = input_tensor.pow(2, out=input_tensor)
print(pow_tensor)
pow_tensor = torch.pow(input_tensor, 2)
print(pow_tensor)
pow_tensor = torch.pow(input_tensor, 2, out=input_tensor)
print(pow_tensor)