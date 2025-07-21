'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
if True:
    input_data = torch.randn(3, 4)
    print(input_data)
    print(torch.nonzero(input_data))
    print(torch.nonzero(input_data, as_tuple=True))