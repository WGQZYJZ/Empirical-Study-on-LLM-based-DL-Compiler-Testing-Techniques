'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
relu_output = torch.nn.functional.relu_(input_data)
print(relu_output)