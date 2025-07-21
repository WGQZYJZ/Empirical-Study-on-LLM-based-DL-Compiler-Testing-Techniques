'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative_\ntorch.Tensor.negative_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[(- 1.0), (- 2.0), (- 3.0)], [1.0, 2.0, 3.0]])
result = torch.Tensor.negative_(input_tensor)
print(result)