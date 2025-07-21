'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty\ntorch.empty(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False, memory_format=torch.contiguous_format)\n'
import torch
input_data = torch.tensor([[3.0, (- 4.0)], [1.0, (- 2.0)]], requires_grad=True)
output = torch.empty(input_data.size())
print('input_data:')
print(input_data)
print('output:')
print(output)