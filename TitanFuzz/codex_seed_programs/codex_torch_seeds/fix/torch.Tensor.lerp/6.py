'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp\ntorch.Tensor.lerp(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.rand(3, 3)
end = torch.rand(3, 3)
weight = torch.rand(1)
output_tensor = input_tensor.lerp(end, weight)
print('output_tensor:', output_tensor)
'\nExpected output:\noutput_tensor: tensor([[0.3270, 0.5454, 0.5642],\n        [0.5246, 0.5128, 0.5519],\n        [0.5459, 0.5103, 0.5239]])\n'