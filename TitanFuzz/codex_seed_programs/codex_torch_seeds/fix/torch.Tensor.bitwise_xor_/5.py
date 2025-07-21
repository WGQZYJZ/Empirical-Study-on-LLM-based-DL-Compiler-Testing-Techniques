'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor_\ntorch.Tensor.bitwise_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
other = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
print('Input 1:', input_tensor)
print('Input 2:', other)
torch.Tensor.bitwise_xor_(input_tensor, other)
print('Output:', input_tensor)