'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input tensor: \n{}'.format(_input_tensor))
_indices = torch.tensor([[0, 0], [1, 1], [2, 2]])
_values = torch.tensor([1, 2, 3])
print('Output tensor: \n{}'.format(_input_tensor.index_put_(_indices, _values, accumulate=False)))
print('Output tensor: \n{}'.format(_input_tensor.index_put_(_indices, _values, accumulate=True)))