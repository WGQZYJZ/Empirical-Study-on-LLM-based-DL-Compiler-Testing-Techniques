'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_data = np.array([[(- 1), (- 2), (- 3)], [3, 4, 5]])
input_data = torch.from_numpy(input_data).float()
output = torch.nn.functional.selu(input_data)
print(output)