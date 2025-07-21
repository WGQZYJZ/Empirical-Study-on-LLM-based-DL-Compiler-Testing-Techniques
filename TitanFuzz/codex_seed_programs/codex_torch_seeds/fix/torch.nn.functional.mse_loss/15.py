"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(4, 10))
target_data = Variable(torch.randn(4, 10))
loss = torch.nn.functional.mse_loss(input_data, target_data)
print(loss)