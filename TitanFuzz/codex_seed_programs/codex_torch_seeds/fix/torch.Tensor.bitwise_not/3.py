'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not\ntorch.Tensor.bitwise_not(_input_tensor)\n'
import torch
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.bool)
print('Input tensor: ', input_tensor)
output_tensor = input_tensor.bitwise_not()
print('Output tensor: ', output_tensor)