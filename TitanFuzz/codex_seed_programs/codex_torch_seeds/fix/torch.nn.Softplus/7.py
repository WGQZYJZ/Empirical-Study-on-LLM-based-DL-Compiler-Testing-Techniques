'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
input_data = torch.randn(20, 10)
softplus = torch.nn.Softplus(beta=1, threshold=20)
output = softplus(input_data)
print(output)