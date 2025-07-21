'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.Tensor([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]]))
print(torch.nn.ReplicationPad1d(padding=2)(input_data))
print(torch.nn.ReplicationPad1d(padding=(1, 2, 3, 4))(input_data))