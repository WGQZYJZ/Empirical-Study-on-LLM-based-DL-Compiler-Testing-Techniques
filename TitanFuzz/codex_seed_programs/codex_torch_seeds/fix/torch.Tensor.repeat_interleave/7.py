'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.repeat_interleave\ntorch.Tensor.repeat_interleave(_input_tensor, repeats, dim=None, *, output_size=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
repeats = torch.tensor([2, 3])
output_tensor = torch.Tensor.repeat_interleave(input_tensor, repeats, dim=0)
print(output_tensor)