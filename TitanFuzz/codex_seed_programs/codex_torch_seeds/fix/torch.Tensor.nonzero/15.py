'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
_input_tensor = torch.Tensor([[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1]])
print('input tensor: \n{}'.format(_input_tensor))
_output_tensor = torch.Tensor.nonzero(_input_tensor, as_tuple=False)
print('output tensor: \n{}'.format(_output_tensor))