'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
_indices = torch.tensor([[0, 1], [1, 2]])
_values = torch.tensor([1.5, 2.5])
_input_tensor.index_put((_indices, _values))
print(_input_tensor)