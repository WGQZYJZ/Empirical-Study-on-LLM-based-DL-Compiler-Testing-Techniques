"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
my_input = torch.randn(4, 3, 32, 32)
print(my_input.shape)
import torch
my_input = torch.randn(4, 3, 32, 32)
print(my_input.shape)
my_output = torch.nn.functional.pad(my_input, (1, 1, 1, 1))
print(my_output.shape)