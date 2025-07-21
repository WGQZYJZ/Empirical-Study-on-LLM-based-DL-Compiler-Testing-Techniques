'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch.nn.functional as F
input_data = np.random.randn(1, 4, 4)
input_data = torch.from_numpy(input_data)
output = F.elu(input_data)
print(output)
output = F.elu_(input_data)
print(output)