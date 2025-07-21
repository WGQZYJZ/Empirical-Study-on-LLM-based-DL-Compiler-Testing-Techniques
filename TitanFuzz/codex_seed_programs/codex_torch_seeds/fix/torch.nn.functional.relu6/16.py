'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu6\ntorch.nn.functional.relu6(input, inplace=False)\n'
import torch
x = torch.rand(1, 3, 4, 4)
out = torch.nn.functional.relu6(x)
print(out)