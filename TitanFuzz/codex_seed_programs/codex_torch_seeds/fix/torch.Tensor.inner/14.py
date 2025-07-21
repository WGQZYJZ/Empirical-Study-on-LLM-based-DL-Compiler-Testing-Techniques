'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inner\ntorch.Tensor.inner(_input_tensor, other)\n'
import torch
if True:
    input_tensor = torch.randn(4, 3)
    other = torch.randn(3)
    print(torch.Tensor.inner(input_tensor, other))