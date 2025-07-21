'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
mask = torch.tensor([[True, False, False], [False, True, False], [False, False, True]], dtype=torch.bool)
source = torch.tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3]], dtype=torch.float32)
input_tensor.masked_scatter_(mask, source)
print(input_tensor)