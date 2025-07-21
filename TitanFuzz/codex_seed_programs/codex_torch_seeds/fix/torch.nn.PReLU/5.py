'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PReLU\ntorch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)\n'
import torch
from torch.nn import PReLU
input_data = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]], dtype=torch.float32)
prelu = PReLU(num_parameters=1, init=0.25)
output = prelu(input_data)
print(output)