'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
import numpy as np
input_data = np.array([(- 1), (- 2), 1, 2])
input_data = torch.tensor(input_data, dtype=torch.float)
print('Input data:', input_data)
output = torch.negative(input_data)
print('Output:', output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reciprocal\ntorch.reciprocal(input, *, out=None)\n'
import torch
import numpy as np
input_data = np.array([(- 1), (- 2), 1, 2])
input_data = torch.tensor(input_data, dtype=torch.float)
print('Input data:', input_data)
output = torch.reciprocal(input_data)
print('Output:', output)