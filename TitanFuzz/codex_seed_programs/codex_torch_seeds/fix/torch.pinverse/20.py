'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
import numpy as np
input_data = torch.randn(3, 5, requires_grad=True)
output = torch.pinverse(input_data)
print(output)
output.backward(torch.ones_like(output))
print(input_data.grad)