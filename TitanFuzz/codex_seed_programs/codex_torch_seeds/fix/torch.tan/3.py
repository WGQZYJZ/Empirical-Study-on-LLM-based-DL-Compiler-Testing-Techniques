'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.0, 3.1416, (- 3.1416)])
print('The input data is: ', input_data)
output = torch.tan(input_data)
print('The output data is: ', output)