'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3))
print('Input tensor:')
print(input_tensor)
mask = torch.tensor([[True, False, False], [False, True, True], [True, False, True]])
source = torch.tensor([1, 2, 3])
torch.Tensor.masked_scatter_(input_tensor, mask, source)
print('Masked scatter:')
print(input_tensor)