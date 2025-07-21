'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor_\ntorch.Tensor.bitwise_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0]])
other = torch.tensor([[1, 0, 0], [0, 0, 1]])
torch.Tensor.bitwise_xor_(input_tensor, other)
print(input_tensor)