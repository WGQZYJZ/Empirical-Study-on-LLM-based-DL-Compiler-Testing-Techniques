'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical\ntorch.Tensor.conj_physical(_input_tensor)\n'
import torch
import torch
input_tensor = torch.tensor([[1, (- 1), 1], [1, 1, (- 1)]])
print('Input tensor:', input_tensor)
output_tensor = input_tensor.conj_physical()
print('Output tensor:', output_tensor)