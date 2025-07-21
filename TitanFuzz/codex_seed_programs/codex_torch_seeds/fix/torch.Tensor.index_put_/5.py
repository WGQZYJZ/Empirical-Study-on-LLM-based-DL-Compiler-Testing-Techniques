'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
from torch.autograd import Variable
import torch
input_tensor = torch.rand(2, 3, 4)
torch.Tensor.index_put_(input_tensor, torch.LongTensor([[0, 1, 2, 1], [1, 0, 1, 2]]), torch.FloatTensor([0, 1, 2, 3]), accumulate=False)
print('input_tensor: ', input_tensor)