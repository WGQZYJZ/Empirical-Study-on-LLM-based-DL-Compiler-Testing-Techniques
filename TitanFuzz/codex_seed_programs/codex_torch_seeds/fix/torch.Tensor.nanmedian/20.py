'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
data = torch.rand(10, 10)
data[0][0] = float('nan')
data[0][1] = float('nan')
data[0][2] = float('nan')
data[0][3] = float('nan')
data[0][4] = float('nan')
data[0][5] = float('nan')
data[0][6] = float('nan')
data[0][7] = float('nan')
data[0][8] = float('nan')
data[0][9] = float('nan')
print(torch.Tensor.nanmedian(data, dim=1, keepdim=True))