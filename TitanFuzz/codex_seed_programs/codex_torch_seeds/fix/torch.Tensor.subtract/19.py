'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[0, 1, 2], [3, 4, 5]])
other = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.subtract(input_tensor, other)
print('The result tensor is: ', output_tensor)