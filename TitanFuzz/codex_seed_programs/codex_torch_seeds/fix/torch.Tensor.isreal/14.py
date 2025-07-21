'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isreal\ntorch.Tensor.isreal(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, 5)
print(input_tensor.isreal())
input_tensor = (torch.randn(10, 5) + (1j * torch.randn(10, 5)))
print(input_tensor.isreal())
input_tensor = (torch.randn(10, 5) + (1j * torch.randn(10, 5)))
print(input_tensor.isreal())
input_tensor = (torch.randn(10, 5) + (1j * torch.randn(10, 5)))
print(input_tensor.isreal())
input_tensor = (torch.randn(10, 5) + (1j * torch.randn(10, 5)))
print(input_tensor.isreal())
input_tensor = (torch.randn(10, 5) + (1j * torch.randn(10, 5)))
print(input_tensor.isreal())