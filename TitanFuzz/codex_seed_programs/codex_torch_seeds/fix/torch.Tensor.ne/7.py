'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ne\ntorch.Tensor.ne(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[(- 1.0), (- 1.0)], [1.0, 1.0]])
print(torch.Tensor.ne(input_tensor, 0.0))