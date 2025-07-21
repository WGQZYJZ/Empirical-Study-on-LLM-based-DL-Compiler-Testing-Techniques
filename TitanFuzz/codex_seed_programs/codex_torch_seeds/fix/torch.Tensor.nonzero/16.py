'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
_input_tensor = torch.tensor([[1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 0, 1]])
_nonzero_tensor_1 = _input_tensor.nonzero()
_nonzero_tensor_2 = _input_tensor.nonzero(as_tuple=True)
print(_nonzero_tensor_1)
print(_nonzero_tensor_2)