'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.AdamW\ntorch.optim.AdamW(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.01, amsgrad=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
y = torch.tensor([[5.0], [6.0]])
optimizer = AdamW([x, y], lr=0.1, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.01, amsgrad=False)
print(optimizer.state_dict())
print(optimizer.param_groups)
print(optimizer.defaults)