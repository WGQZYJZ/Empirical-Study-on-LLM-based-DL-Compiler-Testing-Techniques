'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_not_\ntorch.Tensor.logical_not_(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[1, 0, 1], [1, 1, 0]])
print('\nInput tensor: \n{}'.format(_input_tensor))
_output_tensor = torch.Tensor.logical_not_(_input_tensor)
print('\nOutput tensor: \n{}'.format(_output_tensor))