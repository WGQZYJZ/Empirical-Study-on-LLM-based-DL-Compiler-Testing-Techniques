'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
import torch
import numpy as np
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
weight = torch.tensor([0.2], dtype=torch.float32)
output = torch.nn.functional.prelu(input_data, weight)
print(output)