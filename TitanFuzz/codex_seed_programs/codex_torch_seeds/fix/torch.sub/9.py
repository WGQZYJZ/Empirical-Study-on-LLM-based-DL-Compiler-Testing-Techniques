'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
input_data = torch.tensor([[2.0, 3.0], [4.0, 5.0]])
other_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
result = torch.sub(input_data, other_data)
print('result: ', result)