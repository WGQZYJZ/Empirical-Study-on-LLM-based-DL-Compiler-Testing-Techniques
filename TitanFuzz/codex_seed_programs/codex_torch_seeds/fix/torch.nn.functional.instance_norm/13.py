'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.instance_norm\ntorch.nn.functional.instance_norm(input, running_mean=None, running_var=None, weight=None, bias=None, use_input_stats=True, momentum=0.1, eps=1e-05)\n'
import torch
from torch.autograd import Variable
from torch.nn import functional as F
import torch
input_data = torch.randn(2, 3, 4, 4)
output = F.instance_norm(input_data)
print(output)