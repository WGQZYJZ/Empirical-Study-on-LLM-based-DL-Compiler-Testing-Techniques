'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix_\ntorch.Tensor.fix_(_input_tensor)\n'
import torch
_input_tensor = torch.rand(4, 4)
print('Input tensor: ', _input_tensor)
torch.Tensor.fix_(_input_tensor)
print('Output tensor: ', _input_tensor)