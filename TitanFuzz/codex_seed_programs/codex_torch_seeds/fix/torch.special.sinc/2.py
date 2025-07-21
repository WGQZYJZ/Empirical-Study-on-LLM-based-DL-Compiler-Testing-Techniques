'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.sinc\ntorch.special.sinc(input, *, out=None)\n'
import torch
input_data = torch.tensor([(- 2), (- 1), 0, 1, 2])
print('Input Data: ', input_data)
output_data = torch.special.sinc(input_data)
print('Output Data: ', output_data)