'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
import torch
input_tensor = torch.tensor([(- float('inf')), (- 1.0), 0.0, 1.0, float('inf'), float('nan')])
print(torch.Tensor.isneginf(input_tensor))