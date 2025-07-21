'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[0.0, 1.0], [2.0, 3.0]])
print(torch.Tensor.isinf(_input_tensor))