'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]))
padding = 2
replicationPad1d = torch.nn.ReplicationPad1d(padding)
output = replicationPad1d(input)
print(output)