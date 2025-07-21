'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.map_\ntorch.Tensor.map_(_input_tensor, tensor, callable\n'
import torch
import torch
input_tensor_1 = torch.randint(0, 10, (4, 4))
input_tensor_2 = torch.randint(0, 10, (4, 4))
torch.Tensor.map_(input_tensor_1, input_tensor_2, (lambda x, y: (x + y)))
print(input_tensor_1)