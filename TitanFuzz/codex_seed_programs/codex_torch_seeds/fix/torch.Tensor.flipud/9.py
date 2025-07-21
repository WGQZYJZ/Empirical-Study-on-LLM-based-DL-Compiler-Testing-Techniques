'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flipud\ntorch.Tensor.flipud(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
flip_ud_tensor = torch.Tensor.flipud(input_tensor)
print(flip_ud_tensor)
'\nExpected output:\ntensor([[7., 8., 9.],\n        [4., 5., 6.],\n        [1., 2., 3.]])\n'