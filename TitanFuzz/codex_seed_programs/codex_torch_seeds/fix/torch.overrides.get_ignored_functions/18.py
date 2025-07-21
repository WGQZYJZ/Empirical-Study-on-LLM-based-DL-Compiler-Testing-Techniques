'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.get_ignored_functions\ntorch.overrides.get_ignored_functions()\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
torch.overrides.get_ignored_functions()