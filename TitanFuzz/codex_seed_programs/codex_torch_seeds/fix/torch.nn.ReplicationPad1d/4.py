'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 5))
padding = [1, 2]
output = torch.nn.ReplicationPad1d(padding)(input_data)
print(output)