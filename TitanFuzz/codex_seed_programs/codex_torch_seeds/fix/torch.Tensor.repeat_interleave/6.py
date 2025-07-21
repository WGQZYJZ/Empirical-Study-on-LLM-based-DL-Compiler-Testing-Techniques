'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.repeat_interleave\ntorch.Tensor.repeat_interleave(_input_tensor, repeats, dim=None, *, output_size=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output_tensor = torch.Tensor.repeat_interleave(input_tensor, repeats=2, dim=0)
print('input_tensor:')
print(input_tensor)
print('output_tensor:')
print(output_tensor)