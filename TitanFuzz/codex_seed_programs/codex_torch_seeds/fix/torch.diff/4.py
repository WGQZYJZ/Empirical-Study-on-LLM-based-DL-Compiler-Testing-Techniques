'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diff\ntorch.diff(input, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
diff_data = torch.diff(input_data)
print(diff_data)