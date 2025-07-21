'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
index = torch.tensor([[0, 1], [1, 0]])
output_tensor = torch.Tensor.gather(input_tensor, dim=0, index=index)
print(output_tensor)