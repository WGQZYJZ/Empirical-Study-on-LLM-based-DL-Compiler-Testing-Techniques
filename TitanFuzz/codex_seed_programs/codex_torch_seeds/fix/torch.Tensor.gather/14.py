'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gather\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(2, 3)
'\ntorch.Tensor.gather(_input_tensor, dim, index)\n'
output_tensor = input_tensor.gather(dim=0, index=torch.tensor([[0, 1], [1, 0]]))
print(output_tensor)