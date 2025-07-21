'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor\ntorch.Tensor.bitwise_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0]])
other = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0]])
print(input_tensor.bitwise_xor(other))