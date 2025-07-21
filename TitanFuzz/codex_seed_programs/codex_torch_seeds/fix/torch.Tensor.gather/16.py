'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
output_tensor = torch.Tensor.gather(input_tensor, 1, torch.tensor([[1, 0, 2], [0, 1, 2]]))
print(output_tensor)