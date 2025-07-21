'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
import torch
input_data = torch.tensor([(- 1.0), 0, 1.0])
softplus_fn = torch.nn.Softplus(beta=1, threshold=20)
output = softplus_fn(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0)\n'
import torch
import torch
input_data = torch.tensor([(- 1.0), 0, 1.0])
elu_fn = torch.nn.ELU(alpha=1.0)
output = elu_fn(input_data)
print(output)