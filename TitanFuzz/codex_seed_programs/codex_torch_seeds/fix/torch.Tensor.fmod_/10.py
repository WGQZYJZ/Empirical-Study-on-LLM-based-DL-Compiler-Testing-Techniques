'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmod_\ntorch.Tensor.fmod_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: ', input_tensor)
torch.Tensor.fmod_(input_tensor, 3)
print('Result: ', input_tensor)