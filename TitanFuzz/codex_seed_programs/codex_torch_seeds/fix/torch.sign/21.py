'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
sign_output = torch.sign(input_data)
print('sign_output = ', sign_output)