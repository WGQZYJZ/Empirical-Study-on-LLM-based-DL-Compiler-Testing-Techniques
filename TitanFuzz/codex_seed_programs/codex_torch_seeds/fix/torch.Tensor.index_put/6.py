'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Generate input data:\n', input_tensor)
indices = torch.LongTensor([[0, 1], [2, 3]])
values = torch.FloatTensor([0.5, 0.5])
input_tensor.index_put((indices, indices), values, accumulate=True)
print('Output tensor:\n', input_tensor)