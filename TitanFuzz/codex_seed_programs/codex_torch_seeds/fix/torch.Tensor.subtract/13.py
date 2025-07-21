'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
subtract_output = input_tensor.subtract(other_tensor)
print(subtract_output)
add_output = input_tensor.add(other_tensor)
print(add_output)
div_output = input_tensor.div(other_tensor)
print(div_output)
mul_output = input_tensor.mul(other_tensor)
print(mul_output)
pow_output = input_tensor.pow(other_tensor)
print(pow_output)