'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit\ntorch.Tensor.logit(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(1, 1, 3, 3))
output_data = torch.Tensor.logit(input_data)
print(output_data)