'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
from torch.autograd import Variable
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.subtract_(input_tensor, other=1, alpha=1)
print(output_tensor)