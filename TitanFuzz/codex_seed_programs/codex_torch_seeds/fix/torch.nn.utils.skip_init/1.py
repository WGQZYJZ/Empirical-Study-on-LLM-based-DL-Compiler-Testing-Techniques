'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.skip_init\ntorch.nn.utils.skip_init(module_cls, *args, **kwargs)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(1, 1, 2, 2)
print(input_data)
torch.nn.utils.skip_init(nn.Conv2d, *(1, 1, 2, 2))