'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_not\ntorch.Tensor.logical_not(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[True, False], [True, True]])
output_tensor = torch.Tensor.logical_not(input_tensor)
print(output_tensor)