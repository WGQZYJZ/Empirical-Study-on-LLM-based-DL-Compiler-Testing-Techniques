'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty\ntorch.empty(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False, memory_format=torch.contiguous_format)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4], [5, 6]])
output_data = torch.empty(3, 2)
print('Input data: ', input_data)
print('Output data: ', output_data)