'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lstsq\ntorch.Tensor.lstsq(_input_tensor, A)\n'
import torch
data = torch.randn(5, 3)
matrix = torch.randn(5, 5)
output = data.lstsq(matrix)
print(output)