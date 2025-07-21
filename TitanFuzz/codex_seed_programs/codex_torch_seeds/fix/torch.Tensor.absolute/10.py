'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.absolute\ntorch.Tensor.absolute(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=(- 10), high=10, size=(2, 2))
print('Input Tensor: ', _input_tensor)
_absolute_output = torch.Tensor.absolute(_input_tensor)
print('Absolute Output: ', _absolute_output)