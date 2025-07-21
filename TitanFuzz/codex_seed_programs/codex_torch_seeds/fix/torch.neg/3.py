'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 2), (- 1), 0, 1, 2])
print('Input data: ', input_data)
print('Negative of input data: ', torch.neg(input_data))
output = torch.neg(input_data)
print('Output: ', output)