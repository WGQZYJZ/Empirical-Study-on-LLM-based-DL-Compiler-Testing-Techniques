'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(2, 3, 4), dtype=torch.int32)
print(input_tensor)
cummax_tensor = torch.Tensor.cummax(input_tensor, dim=2)
print(cummax_tensor)