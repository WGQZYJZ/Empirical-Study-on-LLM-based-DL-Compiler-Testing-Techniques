'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
index = torch.LongTensor([[0, 1], [2, 0]])
source = torch.randn(2, 2)
torch.Tensor.put_(_input_tensor, index, source, accumulate=False)
print(_input_tensor)