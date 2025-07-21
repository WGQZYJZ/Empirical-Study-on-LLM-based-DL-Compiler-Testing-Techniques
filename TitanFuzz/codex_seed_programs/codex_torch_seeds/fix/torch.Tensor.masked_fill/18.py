'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
value = torch.tensor(0)
result = input_tensor.masked_fill(mask, value)
print(result)