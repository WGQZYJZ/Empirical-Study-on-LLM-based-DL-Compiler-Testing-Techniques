'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sinc_\ntorch.Tensor.sinc_(_input_tensor)\n'
import torch
from torch.autograd import Function
import torch
input_tensor = torch.rand(1, 1, 5, 5)
torch.Tensor.sinc_(input_tensor)
print(input_tensor)