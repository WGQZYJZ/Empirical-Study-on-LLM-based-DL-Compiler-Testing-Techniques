'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.randn(1, 1, 3)
expanded_tensor = input_tensor.expand(1, 2, 3)
print(expanded_tensor)
'\nExpected output:\ntensor([[[ 0.3985,  0.8160, -1.4790],\n         [ 0.3985,  0.8160, -1.4790]]])\n'