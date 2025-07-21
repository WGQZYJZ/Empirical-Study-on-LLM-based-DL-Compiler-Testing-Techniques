'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
shifts = torch.tensor([1, 1])
dims = torch.tensor([0, 1])
print(input_tensor.roll(shifts, dims))