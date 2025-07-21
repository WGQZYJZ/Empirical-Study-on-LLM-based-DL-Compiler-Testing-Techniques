'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_floating_point\ntorch.is_floating_point(input)\n'
import torch
input = torch.rand(1, 2, 3)
result = torch.is_floating_point(input)
print(result)
'\nOutput:\ntensor([[[0.8474, 0.8989, 0.0291],\n         [0.9888, 0.4102, 0.4190]]], dtype=torch.float64)\n'