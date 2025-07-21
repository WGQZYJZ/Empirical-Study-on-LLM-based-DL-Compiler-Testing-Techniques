'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmod_\ntorch.Tensor.fmod_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randint(1, 10, (4, 4))
print('Input tensor: ', input_tensor)
torch.Tensor.fmod_(input_tensor, 3)
print('Modulo of the tensor: ', input_tensor)