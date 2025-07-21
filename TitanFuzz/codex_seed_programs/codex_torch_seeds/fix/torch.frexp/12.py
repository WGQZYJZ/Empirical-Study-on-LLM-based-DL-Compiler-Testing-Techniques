'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
import torch
input_tensor = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
output_tensor = torch.frexp(input_tensor)
print(output_tensor)