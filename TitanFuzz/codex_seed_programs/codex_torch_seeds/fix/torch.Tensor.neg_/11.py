'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg_\ntorch.Tensor.neg_(_input_tensor)\n'
import torch
from torch.autograd import Variable
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.neg_(input_tensor)
print('output_tensor:', output_tensor)