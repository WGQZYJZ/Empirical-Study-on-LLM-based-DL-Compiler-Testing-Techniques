'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unique_consecutive\ntorch.Tensor.unique_consecutive(_input_tensor, return_inverse=False, return_counts=False, dim=None)\n'
import torch
'\nImport torch\n'
'\nGenerate input data\n'
input_tensor = torch.tensor([[1, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])
'\nCall the API torch.Tensor.unique_consecutive\n'
output_tensor = input_tensor.unique_consecutive()
print(output_tensor)
output_tensor = input_tensor.unique_consecutive(return_inverse=True)
print(output_tensor)
output_tensor = input_tensor.unique_consecutive(return_inverse=True, return_counts=True)
print(output_tensor)
output_tensor = input_tensor.unique_consecutive(return_inverse=True, return_counts=True, dim=0)