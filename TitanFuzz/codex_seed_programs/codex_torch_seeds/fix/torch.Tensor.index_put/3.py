'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
_input_tensor = torch.randn(4, 4)
indices = torch.LongTensor([[0, 1], [2, 3]])
values = torch.FloatTensor([3, 4, 5, 6])
torch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)
print(_input_tensor)