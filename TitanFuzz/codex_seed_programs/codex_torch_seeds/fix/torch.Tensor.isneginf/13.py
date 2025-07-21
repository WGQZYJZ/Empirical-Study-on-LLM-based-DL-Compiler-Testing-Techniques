'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 0.0), (- 1.0), 0.0, 1.0, 2.0, float('inf'), float('nan'), float('-inf')])
result = torch.Tensor.isneginf(input_tensor)
print(result)