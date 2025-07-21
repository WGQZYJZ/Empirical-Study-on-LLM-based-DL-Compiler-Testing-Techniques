'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.absolute\ntorch.absolute(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 1), (- 2), 3], dtype=torch.float32)
print('Input data: ', input_data)
output = torch.absolute(input_data)
print('Output: ', output)