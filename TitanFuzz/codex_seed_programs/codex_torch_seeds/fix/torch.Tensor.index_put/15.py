'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
indices = torch.LongTensor([[0, 1], [1, 2]])
values = torch.randn(2, 2)
torch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)
print(_input_tensor)