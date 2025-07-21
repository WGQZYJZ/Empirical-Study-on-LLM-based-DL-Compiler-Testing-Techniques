'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 4)
print('The dimension of the input tensor is: ', _input_tensor.ndimension())