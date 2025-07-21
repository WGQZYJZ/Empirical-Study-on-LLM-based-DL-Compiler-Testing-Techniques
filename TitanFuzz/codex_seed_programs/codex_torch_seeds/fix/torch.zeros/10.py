'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
if True:
    data = [1, 2, 3, 4, 5]
    tensor = torch.zeros(5)
    print(tensor)