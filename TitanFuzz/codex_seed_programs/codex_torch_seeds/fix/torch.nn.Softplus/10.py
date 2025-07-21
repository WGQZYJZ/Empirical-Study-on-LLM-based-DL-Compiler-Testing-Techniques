'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
input_data = torch.randn(5)
print('Input data:', input_data)
softplus = torch.nn.Softplus()
output_data = softplus(input_data)
print('Output data:', output_data)