'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad3d\ntorch.nn.ReplicationPad3d(padding)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.random.randn(1, 1, 4, 4, 4)
input_data = torch.Tensor(input_data)
pad3d = nn.ReplicationPad3d((1, 1, 1, 1, 1, 1))
output = pad3d(input_data)
print(output)