'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
input_data = torch.randn(3, 4, 5)
output_data = torch.movedim(input_data, 0, (- 1))
print('Input data: ', input_data)
print('Output data: ', output_data)