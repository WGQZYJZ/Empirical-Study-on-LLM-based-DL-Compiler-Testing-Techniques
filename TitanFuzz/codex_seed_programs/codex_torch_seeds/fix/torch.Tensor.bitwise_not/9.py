'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not\ntorch.Tensor.bitwise_not(_input_tensor)\n'
import torch
input_tensor = torch.tensor([True, False, True, False])
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.bitwise_not(input_tensor)
print('Output tensor: ', output_tensor)