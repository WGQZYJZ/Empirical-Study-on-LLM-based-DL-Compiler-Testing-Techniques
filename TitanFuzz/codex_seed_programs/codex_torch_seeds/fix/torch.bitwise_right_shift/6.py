'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
output_data = torch.bitwise_right_shift(input_data, 2)
print(output_data)