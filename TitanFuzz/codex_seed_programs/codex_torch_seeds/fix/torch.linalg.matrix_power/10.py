'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.matrix_power\ntorch.linalg.matrix_power(A, n, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
output_data = torch.linalg.matrix_power(input_data, 2)
print('The input data:\n', input_data)
print('The output data:\n', output_data)