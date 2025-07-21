'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift_\ntorch.Tensor.bitwise_right_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
print(input_tensor)
print(torch.Tensor.bitwise_right_shift_(input_tensor, 2))