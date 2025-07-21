'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[(- 1.0), (- 0.5), 0.0, 1.0, 2.0]]))
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[(- 1.0), (- 0.5), 0.0, 1.0, 2.0]]))
hardtanh = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)
output = hardtanh(input_data)
print('input data: ', input_data)
print('output data: ', output)