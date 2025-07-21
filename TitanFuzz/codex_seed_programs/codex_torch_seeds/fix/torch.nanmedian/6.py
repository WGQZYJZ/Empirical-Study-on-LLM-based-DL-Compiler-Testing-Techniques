'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nanmedian\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(torch.nanmedian(x, dim=(- 1)))
print(torch.nanmedian(x, dim=(- 1), keepdim=True))
print(torch.nanmedian(x, dim=0))
print(torch.nanmedian(x, dim=0, keepdim=True))
'\ntorch.nanmedian(input, dim=-1, keepdim=False, *, out=None)\nParameters:\ninput (Tensor) – the input tensor\ndim (int) – the dimension to reduce\nkeepdim (bool) – whether the output tensor has dim retained or not\nout (Tensor, optional) – the output tensor\n'