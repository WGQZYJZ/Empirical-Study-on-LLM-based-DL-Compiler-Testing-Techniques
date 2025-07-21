'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0e\ntorch.special.i0e(input, *, out=None)\n'
import torch
input = torch.tensor([(- 5), (- 4), (- 3), (- 2), (- 1), 0, 1, 2, 3, 4, 5])
output = torch.special.i0e(input)
print('Input: ', input)
print('Output: ', output)