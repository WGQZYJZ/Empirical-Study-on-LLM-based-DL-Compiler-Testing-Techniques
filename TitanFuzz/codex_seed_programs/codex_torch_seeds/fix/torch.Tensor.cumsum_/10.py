'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum_\ntorch.Tensor.cumsum_(_input_tensor, dim, dtype=None)\n'
import torch
if True:
    input_tensor = torch.randn(2, 3)
    print('input_tensor: ', input_tensor)
    output_tensor = torch.Tensor.cumsum_(input_tensor, dim=0)
    print('output_tensor: ', output_tensor)