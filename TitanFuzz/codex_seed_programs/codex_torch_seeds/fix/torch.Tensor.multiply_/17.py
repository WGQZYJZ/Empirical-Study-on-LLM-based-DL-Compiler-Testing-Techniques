'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply_\ntorch.Tensor.multiply_(_input_tensor, value)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
print('Input tensor:')
print(input_tensor)
output_tensor = input_tensor.multiply_(2)
print('Output tensor:')
print(output_tensor)
print('Input tensor:')
print(input_tensor)