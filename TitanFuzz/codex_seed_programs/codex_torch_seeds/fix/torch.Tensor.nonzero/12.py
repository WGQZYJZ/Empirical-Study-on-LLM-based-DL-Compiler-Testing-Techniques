'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nonzero\ntorch.Tensor.nonzero(_input_tensor, as_tuple=False)\n'
import torch
_input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
non_zero_indices = _input_tensor.nonzero()
print(non_zero_indices)
non_zero_indices = _input_tensor.nonzero(as_tuple=True)
print(non_zero_indices)