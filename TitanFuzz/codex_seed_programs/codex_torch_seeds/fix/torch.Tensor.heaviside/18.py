'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(data)
result = torch.Tensor.heaviside(data, values=1)
print(result)