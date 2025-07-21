'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
elu = torch.nn.ELU(alpha=1.0, inplace=False)
output_data = elu(input_data)
print(output_data)