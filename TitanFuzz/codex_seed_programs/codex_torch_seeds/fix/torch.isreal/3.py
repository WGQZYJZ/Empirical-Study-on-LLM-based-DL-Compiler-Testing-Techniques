'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
input_data = torch.randn(2, 3)
input_data_real = torch.randn(2, 3, dtype=torch.float)
input_data_complex = torch.randn(2, 3, dtype=torch.complex64)
torch.isreal(input_data)
torch.isreal(input_data_real)
torch.isreal(input_data_complex)