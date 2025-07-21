'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSigmoid\ntorch.nn.LogSigmoid()\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.array([(- 10), (- 5), 0, 5, 10])
input_data = torch.from_numpy(input_data).float()
print('Input data: ', input_data)
log_sigmoid = nn.LogSigmoid()
output = log_sigmoid(input_data)
print('Output: ', output)