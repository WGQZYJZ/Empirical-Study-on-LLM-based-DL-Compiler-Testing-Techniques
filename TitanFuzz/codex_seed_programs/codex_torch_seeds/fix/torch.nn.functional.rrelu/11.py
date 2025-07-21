'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
import numpy as np
np.random.seed(42)
input = np.random.randn(10, 10).astype(np.float32)
input = torch.from_numpy(input)
output = torch.nn.functional.rrelu(input)
print(output)