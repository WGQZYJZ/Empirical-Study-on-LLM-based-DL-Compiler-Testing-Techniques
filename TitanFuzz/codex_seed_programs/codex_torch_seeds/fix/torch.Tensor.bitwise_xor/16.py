'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor\ntorch.Tensor.bitwise_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int8)
other = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int8)
torch.Tensor.bitwise_xor(input_tensor, other)