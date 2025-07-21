'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_select\ntorch.Tensor.masked_select(_input_tensor, mask)\n'
import torch
import torch
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
mask = torch.tensor([[0, 0, 1], [1, 0, 0], [0, 0, 1]])
output_tensor = torch.Tensor.masked_select(input_tensor, mask)
print(output_tensor)