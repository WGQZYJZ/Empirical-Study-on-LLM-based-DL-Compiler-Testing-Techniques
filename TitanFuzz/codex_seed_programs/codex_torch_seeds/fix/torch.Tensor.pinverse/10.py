'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pinverse\ntorch.Tensor.pinverse(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, requires_grad=True)
_pinverse_tensor = torch.Tensor.pinverse(_input_tensor)
print('Input Tensor : ', _input_tensor)
print('PInverse Tensor : ', _pinverse_tensor)
'\nTask 4: Call the API torch.pinverse\ntorch.pinverse(_input_tensor)\n'
_input_tensor = torch.randn(2, 3, requires_grad=True)
_pinverse_tensor = torch.pinverse(_input_tensor)
print('Input Tensor : ', _input_tensor)
print('PInverse Tensor : ', _pinverse_tensor)