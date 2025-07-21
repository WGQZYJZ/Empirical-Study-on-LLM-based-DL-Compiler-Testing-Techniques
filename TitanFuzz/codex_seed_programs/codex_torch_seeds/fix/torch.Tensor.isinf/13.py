'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float)
result = torch.Tensor.isinf(data)
print(result)
'\nExpected output:\ntensor([False, False, False, False, False, False, False, False, False, False])\n'