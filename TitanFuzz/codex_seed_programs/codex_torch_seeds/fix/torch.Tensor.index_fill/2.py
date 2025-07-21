'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
x = torch.randn(2, 3)
x.index_fill(0, torch.tensor([0, 2]), 0)