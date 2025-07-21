'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide\ntorch.Tensor.divide(_input_tensor, value, *, rounding_mode=None)\n'
import torch
import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
output_tensor = torch.Tensor.divide(input_tensor, 2.0)
print('The result of division is: {}'.format(output_tensor))