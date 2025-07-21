'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gelu\ntorch.nn.functional.gelu(input)\n'
import torch
import numpy as np
import torch
input = np.array([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
input = torch.tensor(input, dtype=torch.float32)
output = torch.nn.functional.gelu(input)
print(output)