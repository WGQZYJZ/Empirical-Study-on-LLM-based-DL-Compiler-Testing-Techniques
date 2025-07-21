'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
'\nTask 1: Write the code to expand the input tensor to (4, 2, 3)\nTask 2: Write the code to expand the input tensor to (4, 1, 3)\nTask 3: Write the code to expand the input tensor to (4, 2, 1)\n'
expanded_tensor = input_tensor.expand(4, 2, 3)
print(expanded_tensor)
expanded_tensor = input_tensor.expand(4, 1, 3)
print(expanded_tensor)
expanded_tensor = input_tensor.expand(4, 2, 1)
print(expanded_tensor)