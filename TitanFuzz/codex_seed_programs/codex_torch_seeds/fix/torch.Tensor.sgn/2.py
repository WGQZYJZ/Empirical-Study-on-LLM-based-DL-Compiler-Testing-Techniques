'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn\ntorch.Tensor.sgn(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
print(input_tensor.sgn())