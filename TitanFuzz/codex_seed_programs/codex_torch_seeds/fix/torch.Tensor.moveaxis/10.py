'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(2, 3, 4), dtype=torch.int)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.moveaxis(input_tensor, 0, (- 1))
print('Output tensor: \n', output_tensor)