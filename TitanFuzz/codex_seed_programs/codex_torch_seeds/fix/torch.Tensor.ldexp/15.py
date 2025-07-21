'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp\ntorch.Tensor.ldexp(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.randint(low=0, high=2, size=(2, 3))
output_tensor = input_tensor.ldexp(other)
print('The input tensor is: ', input_tensor)
print('The other tensor is: ', other)
print('The output tensor is: ', output_tensor)