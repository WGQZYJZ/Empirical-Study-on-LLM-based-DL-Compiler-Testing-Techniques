'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_tensor = torch.Tensor.det(input_tensor)
print(output_tensor)