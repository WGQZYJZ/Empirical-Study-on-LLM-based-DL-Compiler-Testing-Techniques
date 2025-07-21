'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gt\ntorch.Tensor.gt(_input_tensor, other)\n'
import torch
if True:
    x = torch.tensor([[1, 2, 3], [4, 5, 6]])
    y = torch.tensor([[1, 1, 1], [4, 4, 4]])
    print(x.gt(y))