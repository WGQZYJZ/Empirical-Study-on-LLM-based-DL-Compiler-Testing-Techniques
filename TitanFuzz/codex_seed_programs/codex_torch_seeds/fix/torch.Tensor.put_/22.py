'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
import torch
input_tensor = torch.rand(2, 3, 4, 5)
index = torch.tensor([[0, 1, 2], [1, 2, 3]])
source = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
input_tensor.put_(index, source, accumulate=False)
print(input_tensor)
print('\nThe end of the script!')