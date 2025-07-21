'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmod_\ntorch.Tensor.fmod_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randn(2, 3)
divisor = 3.0
input_tensor.fmod_(divisor)
print('The result is: ', input_tensor)