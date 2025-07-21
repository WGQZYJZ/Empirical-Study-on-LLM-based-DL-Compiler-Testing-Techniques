'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.glu\ntorch.nn.functional.glu(input, dim=-1)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(2, 3, 4)
print(input_data)
output_data = F.glu(input_data, dim=(- 1))
print(output_data)