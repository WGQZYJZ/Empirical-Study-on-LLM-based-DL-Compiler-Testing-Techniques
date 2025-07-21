'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import hardswish
from torch.nn import MSELoss
import torch
input_data = torch.rand(1, 1, 3, 3)
input_data = Variable(input_data, requires_grad=True)
output = hardswish(input_data)
print(output)
mse_loss = MSELoss()
loss = mse_loss(output, input_data)
loss.backward()
print(input_data.grad)