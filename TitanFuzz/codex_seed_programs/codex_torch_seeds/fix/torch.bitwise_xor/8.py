'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input_tensor = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.int32)
other_tensor = torch.tensor([[0, 1], [1, 0], [1, 1], [0, 0]], dtype=torch.int32)
result = torch.bitwise_xor(input_tensor, other_tensor)
print(result)