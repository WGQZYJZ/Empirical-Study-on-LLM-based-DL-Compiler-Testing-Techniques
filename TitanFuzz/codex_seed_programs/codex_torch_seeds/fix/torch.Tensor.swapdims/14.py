'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapdims\ntorch.Tensor.swapdims(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
swap_dim_tensor = input_tensor.swapdims(0, 1)
print(swap_dim_tensor)