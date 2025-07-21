'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.get_ignored_functions\ntorch.overrides.get_ignored_functions()\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
input_size = 4
hidden_size = 8
num_classes = 2
num_epochs = 5
batch_size = 1
learning_rate = 0.001
ignored_functions = torch.overrides.get_ignored_functions()
print('Ignored Functions: ', ignored_functions)