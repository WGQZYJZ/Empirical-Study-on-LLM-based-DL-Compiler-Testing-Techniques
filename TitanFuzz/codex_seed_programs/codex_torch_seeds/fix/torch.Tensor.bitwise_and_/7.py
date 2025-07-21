'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and_\ntorch.Tensor.bitwise_and_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int)
other = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int)
torch.Tensor.bitwise_and_(input_tensor, other)
print(input_tensor)