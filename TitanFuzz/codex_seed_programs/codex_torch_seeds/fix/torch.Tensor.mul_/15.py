'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
input_tensor = torch.randint(1, 10, (3, 3), dtype=torch.int32)
print('Input tensor: ', input_tensor)
torch.Tensor.mul_(input_tensor, 2)
print('Output tensor: ', input_tensor)