'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]], dtype=torch.float)
print(input_data)
log_softmax = nn.LogSoftmax(dim=1)
output_data = log_softmax(input_data)
print(output_data)