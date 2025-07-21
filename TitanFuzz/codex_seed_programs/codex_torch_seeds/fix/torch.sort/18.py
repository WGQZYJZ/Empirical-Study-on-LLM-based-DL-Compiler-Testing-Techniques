'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sort\ntorch.sort(input, dim=-1, descending=False, stable=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('CUDA version: {}'.format(torch.version.cuda))
print('cuDNN version: {}'.format(torch.backends.cudnn.version()))
print('Task 2: Generate input data')
input_data = torch.randn(3, 4)
print('Input data:')
print(input_data)
print('Task 3: Call the API torch.sort')
output_data = torch.sort(input_data, dim=1)
print('Output data:')
print(output_data)