'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.not_equal\ntorch.Tensor.not_equal(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[0, 1], [1, 1], [1, 1], [0, 0]])
other_tensor = torch.tensor([[0, 1], [1, 1], [1, 1], [0, 0]])
output_tensor = torch.Tensor.not_equal(input_tensor, other_tensor)
print('input_tensor:')
print(input_tensor)
print('other_tensor:')
print(other_tensor)
print('output_tensor:')
print(output_tensor)