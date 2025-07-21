'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.uniform_\ntorch.Tensor.uniform_(_input_tensor, from=0, to=1)\n'
import torch
input_tensor = torch.Tensor(2, 3)
print(input_tensor)
input_tensor.uniform_(from_=0, to=1)
print(input_tensor)