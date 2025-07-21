'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit\ntorch.Tensor.logit(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[2, 3, 4], [5, 6, 7]])
result = input_tensor.logit()
print(result)
print(type(result))