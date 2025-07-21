'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input data:')
print(_input_tensor)
indices = torch.tensor([[0, 0], [1, 2]])
values = torch.tensor([1.0, 2.0])
_input_tensor.index_put(indices, values, accumulate=False)
print('Output data:')
print(_input_tensor)