'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_complex\ntorch.is_complex(input)\n'
import torch
input_data = torch.randn(1, 2, 3, 4)
print(torch.is_complex(input_data))
input_data = torch.randn(1, 2, 3, 4, dtype=torch.complex64)
print(torch.is_complex(input_data))