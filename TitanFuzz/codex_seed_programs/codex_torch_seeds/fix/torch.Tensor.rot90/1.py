'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rot90\ntorch.Tensor.rot90(_input_tensor, k, dims)\n'
import torch
import torch
input_tensor = torch.randn(3, 3, 3)
output_tensor = torch.Tensor.rot90(input_tensor, 2, (1, 2))
print(output_tensor)