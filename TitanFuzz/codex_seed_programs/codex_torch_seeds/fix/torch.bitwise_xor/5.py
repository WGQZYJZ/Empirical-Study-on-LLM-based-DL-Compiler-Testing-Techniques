'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_xor\ntorch.bitwise_xor(input, other, *, out=None)\n'
import torch
input_data = torch.randint(0, 2, (10,))
other_data = torch.randint(0, 2, (10,))
print('input_data:', input_data)
print('other_data:', other_data)
output_data = torch.bitwise_xor(input_data, other_data)
print('output_data:', output_data)