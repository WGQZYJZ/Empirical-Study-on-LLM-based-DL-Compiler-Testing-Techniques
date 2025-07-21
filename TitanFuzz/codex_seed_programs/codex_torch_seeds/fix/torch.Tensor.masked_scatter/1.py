'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
input_tensor = torch.randn(3, 3, dtype=torch.float)
print(input_tensor)
mask = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=torch.uint8)
print(mask)
tensor = torch.tensor([1, 2, 3], dtype=torch.float)
print(tensor)
output_tensor = torch.Tensor.masked_scatter(input_tensor, mask, tensor)
print(output_tensor)