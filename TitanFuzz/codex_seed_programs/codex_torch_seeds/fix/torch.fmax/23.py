'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
other_data = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
output_data = torch.fmax(input_data, other_data)
print('input:')
print(input_data)
print('other:')
print(other_data)
print('output:')
print(output_data)