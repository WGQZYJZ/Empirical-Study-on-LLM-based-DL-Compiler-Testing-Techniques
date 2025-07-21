'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copysign_\ntorch.Tensor.copysign_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, (- 1), 3, (- 3)], [4, (- 4), 6, (- 6)]])
other = torch.tensor([[1, 1, 1, 1], [1, 1, 1, 1]])
output_tensor = torch.Tensor.copysign_(input_tensor, other)
print(output_tensor)