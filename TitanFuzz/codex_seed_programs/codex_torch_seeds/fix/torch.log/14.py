'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log\ntorch.log(input, *, out=None)\n'
import torch
input_data = torch.tensor([2.0, 2.0, 2.0, 2.0, 2.0])
print('Input data: ', input_data)
log_value = torch.log(input_data)
print('Output value: ', log_value)