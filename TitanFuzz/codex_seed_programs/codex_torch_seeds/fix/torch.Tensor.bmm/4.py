'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bmm\ntorch.Tensor.bmm(_input_tensor, batch2)\n'
import torch
_input_tensor = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
torch.Tensor.bmm(_input_tensor, batch2)