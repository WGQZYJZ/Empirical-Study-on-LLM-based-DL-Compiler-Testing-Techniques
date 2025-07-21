'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones\ntorch.ones(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.ones(2, 3)
print(input_data)
output_data = torch.ones(2, 3)
print(output_data)
if torch.equal(input_data, output_data):
    print('The input and output data are the same.')
else:
    print('The input and output data are different.')