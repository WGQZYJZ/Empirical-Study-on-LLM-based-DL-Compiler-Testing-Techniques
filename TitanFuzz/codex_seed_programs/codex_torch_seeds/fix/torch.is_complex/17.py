'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_complex\ntorch.is_complex(input)\n'
import torch
input1 = torch.randn(2, 3)
input2 = (torch.randn(2, 3) + (1j * torch.randn(2, 3)))
print('Is input1 complex? ', torch.is_complex(input1))
print('Is input2 complex? ', torch.is_complex(input2))