'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil_\ntorch.Tensor.ceil_(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([(- 1.8), (- 1.5), (- 0.2), 0.2, 1.5, 1.8, 2.0])
print('Input tensor: ', _input_tensor)
print('Ceil of the input tensor: ', torch.Tensor.ceil_(_input_tensor))