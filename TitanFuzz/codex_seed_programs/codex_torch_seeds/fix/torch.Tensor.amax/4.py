'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amax\ntorch.Tensor.amax(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
max_value = input_tensor.amax()
print(max_value)
max_value = input_tensor.amax(dim=1)
print(max_value)
max_value = input_tensor.amax(dim=1, keepdim=True)
print(max_value)
max_value = input_tensor.amax(dim=0)
print(max_value)
max