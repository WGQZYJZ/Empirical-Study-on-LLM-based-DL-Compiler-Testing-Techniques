'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_tensor = torch.randint(0, 10, (2, 3, 4))
print(input_tensor)
swap_tensor = input_tensor.swapaxes(0, 1)
print(swap_tensor)