'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[(- 1), (- 2), 3, 4]]))
relu6 = torch.nn.ReLU6(inplace=False)
print('Input data: ', input_data)
print('Output of the API: ', relu6(input_data))