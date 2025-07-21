'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.array([(- 1), 0, 1, 2, 3, 4])
input_data = torch.tensor(input_data, dtype=torch.float32)
elu = nn.ELU()
output = elu(input_data)
print(output)