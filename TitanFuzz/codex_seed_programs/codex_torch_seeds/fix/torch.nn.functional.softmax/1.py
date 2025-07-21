'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softmax\ntorch.nn.functional.softmax(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
import numpy as np
print(torch.__version__)
x = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]], dtype=torch.float32)
print(x)
output = torch.nn.functional.softmax(x, dim=1)
print(output)
print(np.sum(output.numpy(), axis=1))