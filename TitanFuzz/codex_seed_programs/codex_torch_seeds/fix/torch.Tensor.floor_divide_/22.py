'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide_\ntorch.Tensor.floor_divide_(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(4, 4)
value = 2
torch.Tensor.floor_divide_(input_tensor, value)
print(input_tensor)