'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
import numpy as np
input_data = np.random.randn(1, 3, 4, 4)
input_data = torch.tensor(input_data, dtype=torch.float32)
out = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)(input_data)
print(out)