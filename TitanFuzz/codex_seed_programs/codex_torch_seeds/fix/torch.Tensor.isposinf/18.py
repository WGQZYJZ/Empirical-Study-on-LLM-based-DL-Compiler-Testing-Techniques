'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isposinf\ntorch.Tensor.isposinf(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
result = torch.Tensor.isposinf(_input_tensor)
print(result)