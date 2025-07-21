'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6]]]))
replication_pad1d = torch.nn.ReplicationPad1d(padding=2)
output = replication_pad1d(input_data)
print(output)