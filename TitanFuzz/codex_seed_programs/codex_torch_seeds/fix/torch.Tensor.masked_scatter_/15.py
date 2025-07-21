'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
mask = torch.tensor([[True, True, False], [False, False, True]], dtype=torch.uint8)
source = torch.tensor([[9, 9], [6, 6]], dtype=torch.float32)
torch.Tensor.masked_scatter_(input_tensor, mask, source)
print(input_tensor)