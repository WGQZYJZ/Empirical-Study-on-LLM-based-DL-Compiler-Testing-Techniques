'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor(1, 1, 3, 3))
torch.nn.init.zeros_(input_data)
print(input_data)
torch.nn.init.ones_(input_data)
print(input_data)
torch.nn.init.normal_(input_data)
print(input_data)
torch.nn.init.uniform_(input_data)
print(input_data)