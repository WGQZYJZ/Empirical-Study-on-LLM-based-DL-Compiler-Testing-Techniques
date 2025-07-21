'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
input_data = torch.randn(2, 2)
print(input_data)
print(torch.nn.functional.softplus(input_data))