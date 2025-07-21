'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 2))
print(input_data)
output_data = torch.nn.functional.elu(input_data)
print(output_data)