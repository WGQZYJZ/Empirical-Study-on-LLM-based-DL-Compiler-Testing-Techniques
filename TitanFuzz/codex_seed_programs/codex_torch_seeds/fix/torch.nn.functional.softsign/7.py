'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softsign\ntorch.nn.functional.softsign(input)\n'
import torch
from torch.autograd import Variable
import torch
input_data = torch.randn(5)
print('input_data: ', input_data)
output_data = torch.nn.functional.softsign(input_data)
print('output_data: ', output_data)