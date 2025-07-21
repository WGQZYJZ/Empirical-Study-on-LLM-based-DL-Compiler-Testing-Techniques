'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
input_tensor = torch.tensor([[2, 3], [4, 5]])
output_tensor = input_tensor.matrix_power(2)
print(output_tensor)