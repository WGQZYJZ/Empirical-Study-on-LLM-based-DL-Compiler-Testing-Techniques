'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze\ntorch.Tensor.unsqueeze(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
print(input_tensor.unsqueeze(0))
print(input_tensor.unsqueeze(1))
print(input_tensor.unsqueeze(2))
print(input_tensor.unsqueeze((- 1)))
print(input_tensor.unsqueeze((- 2)))
print(input_tensor.unsqueeze((- 3)))