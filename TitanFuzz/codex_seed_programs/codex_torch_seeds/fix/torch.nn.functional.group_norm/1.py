'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.group_norm\ntorch.nn.functional.group_norm(input, num_groups, weight=None, bias=None, eps=1e-05)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input_data = np.random.randn(2, 4, 5, 6)
input_data = torch.FloatTensor(input_data)
output = F.group_norm(input_data, num_groups=2, weight=None, bias=None, eps=1e-05)
print(output)