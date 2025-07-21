'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_select\ntorch.Tensor.masked_select(_input_tensor, mask)\n'
import torch
input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
mask = torch.tensor([[0, 1], [1, 0]])
output_tensor = torch.Tensor.masked_select(input_tensor, mask)
print(output_tensor)