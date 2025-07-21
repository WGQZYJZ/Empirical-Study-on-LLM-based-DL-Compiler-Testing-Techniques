'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not_\ntorch.Tensor.bitwise_not_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[0, 1, 0], [1, 1, 0], [1, 1, 1]], dtype=torch.bool)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)
print('Output tensor: ', output_tensor)