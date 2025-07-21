'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder_\ntorch.Tensor.remainder_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(2, 3), dtype=torch.int32)
print('Input tensor: ', input_tensor)
torch.Tensor.remainder_(input_tensor, divisor=2)
print('The remainder of division by 2 of each element in the tensor: ', input_tensor)