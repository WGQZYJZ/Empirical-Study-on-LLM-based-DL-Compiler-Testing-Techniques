'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
_input_tensor = torch.randn(3, 3)
_dim = 1
_index = torch.tensor([0, 2])
_value = 2.0
torch.Tensor.index_fill(_input_tensor, _dim, _index, _value)
print(_input_tensor)