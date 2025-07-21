'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
import torch.nn.functional as F
input_data = torch.rand(5, 3)
output_data = F.softplus(input_data)
print(output_data)