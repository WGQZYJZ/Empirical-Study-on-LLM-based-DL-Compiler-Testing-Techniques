'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.maximum\ntorch.Tensor.maximum(_input_tensor, other)\n'
import torch
if True:
    input_tensor = torch.randn(1, 3)
    other = torch.randn(1, 3)
    print(torch.Tensor.maximum(input_tensor, other))