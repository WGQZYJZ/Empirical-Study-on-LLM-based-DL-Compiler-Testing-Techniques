'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
input_data = Variable(torch.randn(5, 5))
output = F.layer_norm(input_data, [5], eps=1e-05)
print(output)