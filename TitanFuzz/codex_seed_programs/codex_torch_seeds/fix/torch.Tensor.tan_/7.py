'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tan_\ntorch.Tensor.tan_(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
input_tensor = torch.rand(5, 3)
print(input_tensor)
torch.Tensor.tan_(input_tensor)
print(input_tensor)