'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
print(torch.__version__)
input_tensor = torch.randn(3, 4)
index = torch.tensor([[0, 1, 2, 0], [2, 0, 0, 1]])
src = torch.tensor([[1, 0, (- 1), 1], [1, (- 1), 1, 0]])
print(input_tensor)
print(index)
print(src)
output_tensor = torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src)
print(output_tensor)