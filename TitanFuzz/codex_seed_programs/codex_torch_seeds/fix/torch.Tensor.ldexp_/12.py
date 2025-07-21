'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp_\ntorch.Tensor.ldexp_(_input_tensor, other)\n'
import torch
if True:
    data = torch.rand(1, 3, 4, 5)
    print(data)
    print(data.ldexp_(2))