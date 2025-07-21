"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_uniform_\ntorch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch
import torch.nn as nn
from torch.autograd import Variable
input = Variable(torch.randn(20, 20))
torch.nn.init.kaiming_uniform_(input)
print(input)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch
import torch.nn as nn
from torch.autograd import Variable