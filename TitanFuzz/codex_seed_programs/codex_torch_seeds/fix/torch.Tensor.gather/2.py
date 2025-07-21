'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = torch.Tensor.gather(input_tensor, 0, torch.tensor([[0, 0], [1, 0]]))
print(output_tensor)