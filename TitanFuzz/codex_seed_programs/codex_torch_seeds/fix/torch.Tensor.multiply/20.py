'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.multiply(input_tensor, 2)
print('output_tensor: ', output_tensor)
output_tensor = torch.Tensor.multiply(input_tensor, 0.5)
print('output_tensor: ', output_tensor)
output_tensor = torch.Tensor.multiply(input_tensor, (- 1))
print('output_tensor: ', output_tensor)