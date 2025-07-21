'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu_\ntorch.nn.functional.elu_(input, alpha=1.)\n'
import torch
input_data = torch.randn(10)
input_data
torch.nn.functional.elu_(input_data)
torch.nn.functional.elu(input_data)
torch.nn.functional.elu(input_data, alpha=0.5)