'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import torch.nn as nn
import numpy as np
input = np.random.uniform(size=(1, 3, 5, 5))
input = torch.from_numpy(input).float()
elu = nn.ELU(alpha=1.0, inplace=False)
elu_inplace = nn.ELU(alpha=1.0, inplace=True)
elu_alpha = nn.ELU(alpha=0.5, inplace=False)
output = elu(input)
output_inplace = elu_inplace(input)
output_alpha = elu_alpha(input)
print(output)
print(output_inplace)
print(output_alpha)