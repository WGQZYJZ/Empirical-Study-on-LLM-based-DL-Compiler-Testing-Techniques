'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty\ntorch.empty(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False, memory_format=torch.contiguous_format)\n'
import torch
input_data = torch.zeros(5, 3, dtype=torch.long)
print(input_data)
output_data = torch.empty(5, 3)
torch.add(input_data, input_data, out=output_data)
print(output_data)
input_data.add_(input_data)
print(input_data)
print(input_data.size())
print(input_data.view(15))
print(input_data.view((- 1), 5))
print(input_data[(1, 1)].item())