'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
print(input_tensor)
output_tensor = torch.Tensor.tile(input_tensor, dims=[1, 2])
print(output_tensor)