'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
import numpy as np
import torch
input_data = torch.rand(2, 3)
print(torch.nn.Softmin(dim=0)(input_data))
print(torch.nn.Softmin(dim=1)(input_data))
print(torch.nn.Softmin(dim=None)(input_data))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
import numpy as np
import torch
input_data = torch.rand(2, 3)
print(torch.nn.Softplus(beta=1, threshold=20)(input_data))
print(torch.nn.Softplus(beta=2, threshold=20)(input_data))