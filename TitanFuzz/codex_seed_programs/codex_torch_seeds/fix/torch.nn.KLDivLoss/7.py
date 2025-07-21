"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 10))
target_data = Variable(torch.randn(5, 10))
print(input_data)
print(target_data)
loss_fn = torch.nn.KLDivLoss()
loss = loss_fn(input_data, target_data)
print(loss)