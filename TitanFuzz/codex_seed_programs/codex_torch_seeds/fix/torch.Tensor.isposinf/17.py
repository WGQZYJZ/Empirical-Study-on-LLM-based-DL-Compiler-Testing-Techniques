'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isposinf\ntorch.Tensor.isposinf(_input_tensor)\n'
import torch
input_tensor = torch.tensor([float('inf'), float('-inf'), float('nan'), float('inf'), float('inf')])
result = torch.Tensor.isposinf(input_tensor)
print(result)