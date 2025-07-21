'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch
input = Variable(torch.randn(2, 3))
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=True, inplace=False)
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=True, inplace=True)
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=True)
torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)