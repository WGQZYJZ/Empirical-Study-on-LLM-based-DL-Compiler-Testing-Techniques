'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix\ntorch.Tensor.fix(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
_fixed_tensor = torch.Tensor.fix(_input_tensor)
print('Input tensor: ', _input_tensor)
print('Fixed tensor: ', _fixed_tensor)