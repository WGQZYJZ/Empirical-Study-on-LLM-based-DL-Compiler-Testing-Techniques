'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
input = Variable(torch.randn(2, 3))
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_in\ntorch.nn.functional.feature_alpha_in(input, alpha=1.0, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
input = Variable(torch.randn(2, 3))