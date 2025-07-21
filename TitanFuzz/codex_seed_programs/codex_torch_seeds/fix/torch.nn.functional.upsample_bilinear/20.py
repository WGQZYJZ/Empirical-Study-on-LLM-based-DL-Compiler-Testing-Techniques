'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
import torch.nn.functional as F
input = torch.Tensor([[[[1, 2, 3], [4, 5, 6]]]])
upsample_bilinear = F.upsample_bilinear(input, scale_factor=2)
print('input: ', input)
print('upsample_bilinear: ', upsample_bilinear)