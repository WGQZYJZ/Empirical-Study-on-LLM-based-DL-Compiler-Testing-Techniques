'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.topk\ntorch.Tensor.topk(_input_tensor, k, dim=None, largest=True, sorted=True)\n'
import torch
input_tensor = torch.randn(3, 5)
print('Input tensor:')
print(input_tensor)
k = 3
dim = 1
largest = True
sorted = True
output_tensor = torch.Tensor.topk(input_tensor, k, dim, largest, sorted)
print('Output tensor:')
print(output_tensor)
print('Top 3 values and their indices in the first row of the input tensor:')
print(output_tensor[0])
print('Top 3 values and their indices in the second row of the input tensor:')
print(output_tensor[1])