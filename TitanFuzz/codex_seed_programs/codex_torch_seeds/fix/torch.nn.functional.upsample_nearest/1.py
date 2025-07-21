'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
x = torch.tensor([[[1, 2, 3], [4, 5, 6]]], dtype=torch.float32)
print('Input data: ', x)
y = F.upsample_nearest(x, scale_factor=2)
print('Output data: ', y)