'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
if True:
    input_tensor = torch.arange(1, 11, dtype=torch.float)
    print('input_tensor: ', input_tensor)
    diff_tensor = input_tensor.diff(dim=0)
    print('diff_tensor: ', diff_tensor)
    diff_tensor = input_tensor.diff(dim=0, prepend=input_tensor[0], append=input_tensor[(- 1)])
    print('diff_tensor: ', diff_tensor)