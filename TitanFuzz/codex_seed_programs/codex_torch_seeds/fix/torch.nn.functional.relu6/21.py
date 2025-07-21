'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu6\ntorch.nn.functional.relu6(input, inplace=False)\n'
import torch
import torch.nn.functional as F
input_data = torch.randn(1, 1, 4, 4)
out = F.relu6(input_data)
print(out)