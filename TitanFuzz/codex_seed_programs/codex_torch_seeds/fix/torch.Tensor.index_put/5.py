'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
_input_tensor = torch.rand(4, 4)
_indices = torch.tensor([[1, 2], [2, 3]])
_values = torch.tensor([[1, 2], [3, 4]])
torch.Tensor.index_put(_input_tensor, _indices, _values, accumulate=False)
print(_input_tensor)