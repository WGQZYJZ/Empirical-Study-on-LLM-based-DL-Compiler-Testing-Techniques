'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardsigmoid\ntorch.nn.Hardsigmoid(inplace=False)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.array([[(- 2), 3, 2, (- 1)]])
input = torch.tensor(input_data, dtype=torch.float)
hardsigmoid = nn.Hardsigmoid()
output = hardsigmoid(input)
print('input:', input)
print('output:', output)