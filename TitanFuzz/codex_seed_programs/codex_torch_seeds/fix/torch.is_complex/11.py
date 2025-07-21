'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_complex\ntorch.is_complex(input)\n'
import torch
input = torch.randn(3, 4)
print(input)
output = torch.is_complex(input)
print(output)