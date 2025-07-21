'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
input = torch.randn(20, 16, 50, 32, 45)
output = torch.nn.FractionalMaxPool3d(kernel_size=(3, 5, 3), output_size=(5, 10, 3))(input)
print('input: ', input.shape)
print('output: ', output.shape)