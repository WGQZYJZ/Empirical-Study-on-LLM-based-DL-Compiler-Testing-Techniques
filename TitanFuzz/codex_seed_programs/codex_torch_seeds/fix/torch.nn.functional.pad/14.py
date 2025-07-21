"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
import torch.nn.functional as F
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input)
'\nTask 4: padding with 0\n'
print(F.pad(input, (1, 1)))
'\nTask 5: padding with 0 on the left side\n'
print(F.pad(input, (1, 0)))
'\nTask 6: padding with 0 on the right side\n'
print(F.pad(input, (0, 1)))
'\nTask 7: padding with 0 on the top side\n'
print(F.pad(input, (1, 0, 0, 0)))
'\nTask 8: padding with 0 on the bottom side\n'
print(F.pad(input, (0, 0, 1, 0)))
'\nTask 9: padding with 0 on the left and right sides\n'
print(F.pad(input, (1, 1, 0, 0)))
'\nTask 10: padding with 0 on the top and bottom sides\n'