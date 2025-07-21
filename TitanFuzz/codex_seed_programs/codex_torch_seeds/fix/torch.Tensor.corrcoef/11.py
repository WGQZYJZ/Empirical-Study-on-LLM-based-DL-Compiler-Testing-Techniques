'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.corrcoef\ntorch.Tensor.corrcoef(_input_tensor)\n'
import torch
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
y = torch.Tensor([[0, 2, 1], [7, 5, 3]])
print(torch.Tensor.corrcoef(x, y))