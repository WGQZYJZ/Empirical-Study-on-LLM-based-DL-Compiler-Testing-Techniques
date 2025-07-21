'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
x.index_fill_(1, torch.LongTensor([0, 2]), 0)
print(x)
x.index_fill_(0, torch.LongTensor([0, 1]), 0)
print(x)