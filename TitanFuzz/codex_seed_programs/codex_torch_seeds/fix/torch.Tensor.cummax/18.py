'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
import torch
input_tensor = torch.randint(10, (3, 4))
print(input_tensor)
output_tensor = input_tensor.cummax(dim=1)
print(output_tensor)