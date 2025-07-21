'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
import numpy as np
data = np.random.randn(1, 2, 3, 3)
data = torch.Tensor(data)
out = torch.nn.Threshold(0.5, 0.0)(data)
print(out)