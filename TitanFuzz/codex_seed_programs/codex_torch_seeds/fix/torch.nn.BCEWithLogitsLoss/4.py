"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BCEWithLogitsLoss\ntorch.nn.BCEWithLogitsLoss(weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3))
target = Variable(torch.FloatTensor(2, 3).random_(2))
loss = torch.nn.BCEWithLogitsLoss()
output = loss(input_data, target)
print(output)
loss = torch.nn.BCELoss()
output = loss(torch.sigmoid(input_data), target)
print(output)