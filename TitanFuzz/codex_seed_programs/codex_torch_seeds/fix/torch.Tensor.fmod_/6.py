'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmod_\ntorch.Tensor.fmod_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randn(3, 3)
divisor = torch.tensor(2)
torch.Tensor.fmod_(input_tensor, divisor)
print('input_tensor:', input_tensor)