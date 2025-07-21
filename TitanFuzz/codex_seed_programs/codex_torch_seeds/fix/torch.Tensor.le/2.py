'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.le\ntorch.Tensor.le(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
output_tensor = input_tensor.le(5)
print(output_tensor)
output_tensor = input_tensor.le(7)
print(output_tensor)
output_tensor = input_tensor.le(10)
print(output_tensor)
output_tensor = input_tensor.le(0)
print(output_tensor)
output_tensor = input_tensor.le(100)
print(output_tensor)