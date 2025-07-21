'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fmod_\ntorch.Tensor.fmod_(_input_tensor, divisor)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input tensor: ', _input_tensor)
torch.Tensor.fmod_(_input_tensor, 2)
print('Modulo of input tensor with 2: ', _input_tensor)
torch.Tensor.fmod_(_input_tensor, 3)
print('Modulo of input tensor with 3: ', _input_tensor)
torch.Tensor.fmod_(_input_tensor, 4)
print('Modulo of input tensor with 4: ', _input_tensor)
torch.Tensor.fmod_(_input_tensor, 5)
print('Modulo of input tensor with 5: ', _input_tensor)