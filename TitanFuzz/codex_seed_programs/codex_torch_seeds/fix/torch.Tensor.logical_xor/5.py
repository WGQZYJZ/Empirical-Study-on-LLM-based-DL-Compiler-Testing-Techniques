'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor\ntorch.Tensor.logical_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, False], [False, True]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other=True)
print(output_tensor)