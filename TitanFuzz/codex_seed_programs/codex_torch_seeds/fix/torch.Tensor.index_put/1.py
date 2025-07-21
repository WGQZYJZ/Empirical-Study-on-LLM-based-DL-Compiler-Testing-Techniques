'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
'\nTask 1:\n'
'\nTask 2:\n'
_input_tensor = torch.randn(1, 3, 4, 4)
print(_input_tensor)
'\nTask 3:\n'
indices = torch.LongTensor([[0, 1, 2, 3], [0, 1, 2, 3]])
values = torch.randn(2, 4)
print(indices)
print(values)
_input_tensor.index_put((0, 1, 2, 3), indices, values, accumulate=False)
print(_input_tensor)