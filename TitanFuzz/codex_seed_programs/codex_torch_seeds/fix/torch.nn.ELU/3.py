'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([(- 1), 0, 1, 2, 3, 4, 5], dtype=torch.float32)
elu = nn.ELU(alpha=1.0, inplace=False)
output_data = elu(input_data)
print(output_data)
print(output_data.grad_fn)