'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout2d\ntorch.nn.functional.dropout2d(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 10, 10))
dropout_output = F.dropout2d(input_data, p=0.5, training=True, inplace=False)
print('The shape of input data is: {}'.format(input_data.shape))
print('The shape of dropout output is: {}'.format(dropout_output.shape))