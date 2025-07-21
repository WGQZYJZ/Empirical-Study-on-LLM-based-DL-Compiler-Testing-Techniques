"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8]]))
target_data = Variable(torch.LongTensor([0, 1]))
loss = torch.nn.CrossEntropyLoss()
output = loss(input_data, target_data)
print(output)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CrossEntropyLoss\ntorch.nn.CrossEntropyLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch