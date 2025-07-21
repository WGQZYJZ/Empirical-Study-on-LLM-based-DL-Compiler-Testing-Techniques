'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative\ntorch.Tensor.negative(_input_tensor)\n'
import torch
_input_tensor = torch.rand(4, 4)
print('Input tensor: ', _input_tensor)
_negative_tensor = torch.Tensor.negative(_input_tensor)
print('Negative tensor: ', _negative_tensor)