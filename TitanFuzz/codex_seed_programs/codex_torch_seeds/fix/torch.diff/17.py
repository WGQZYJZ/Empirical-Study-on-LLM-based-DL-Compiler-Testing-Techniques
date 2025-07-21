'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diff\ntorch.diff(input, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print('input data:')
print(input_data)
diff_data = torch.diff(input_data)
print('diff data:')
print(diff_data)