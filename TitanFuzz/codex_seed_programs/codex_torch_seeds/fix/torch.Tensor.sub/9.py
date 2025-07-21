'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor(10)
result_tensor = input_tensor.sub(other)
print(result_tensor)