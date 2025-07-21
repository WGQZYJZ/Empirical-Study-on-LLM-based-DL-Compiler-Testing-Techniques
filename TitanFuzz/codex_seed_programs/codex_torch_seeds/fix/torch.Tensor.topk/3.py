'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.topk\ntorch.Tensor.topk(_input_tensor, k, dim=None, largest=True, sorted=True)\n'
import torch
import torch
input_tensor = torch.randn(3, 4)
k = 2
dim = 1
largest = True
sorted = True
output_tensor = input_tensor.topk(k, dim, largest, sorted)
print('input_tensor:')
print(input_tensor)
print('output_tensor:')
print(output_tensor)