'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal_\ntorch.Tensor.reciprocal_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0])
torch.Tensor.reciprocal_(input_tensor)
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder_\ntorch.Tensor.remainder_(_input_tensor, _divisor)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0])
divisor = torch.tensor([2.0])
torch.Tensor.remainder_(input_tensor, divisor)