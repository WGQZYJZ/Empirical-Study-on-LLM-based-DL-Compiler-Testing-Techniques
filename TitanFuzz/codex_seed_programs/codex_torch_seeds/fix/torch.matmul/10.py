'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matmul\ntorch.matmul(input, other, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('CUDA version: {}'.format(torch.version.cuda))
print('cuDNN version: {}'.format(torch.backends.cudnn.version()))
print()
print('Task 2: Generate input data')
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other_data = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
print('input_data: {}'.format(input_data))
print('other_data: {}'.format(other_data))
print()
print('Task 3: Call the API torch.matmul')
output_data = torch.matmul(input_data, other_data)
print