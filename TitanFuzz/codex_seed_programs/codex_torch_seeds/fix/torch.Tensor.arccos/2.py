'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos\ntorch.Tensor.arccos(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
input_tensor = Variable(torch.randn(1, 3))
output_tensor = torch.Tensor.arccos(input_tensor)
print(output_tensor)