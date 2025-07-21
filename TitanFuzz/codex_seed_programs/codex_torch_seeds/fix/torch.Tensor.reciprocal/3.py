'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
input_data = torch.tensor([2.0, 4.0, 8.0, 16.0])
result = input_data.reciprocal()
print(result)