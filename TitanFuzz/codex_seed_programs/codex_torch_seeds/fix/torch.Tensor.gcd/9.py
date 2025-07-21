'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd\ntorch.Tensor.gcd(_input_tensor, other)\n'
import torch
input_data = torch.randint(low=0, high=10, size=(5,))
print(torch.Tensor.gcd(input_data, other=5))