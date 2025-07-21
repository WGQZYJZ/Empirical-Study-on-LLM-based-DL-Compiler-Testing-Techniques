'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
import torch
input_tensor = torch.randn(20, 16, 50, 32, 45)
torch.nn.FractionalMaxPool3d(kernel_size=(5, 10, 3), output_size=(5, 5, 5))(input_tensor)
print('Task 3: Call the API torch.nn.FractionalMaxPool3d')
print('torch.nn.FractionalMaxPool3d(kernel_size=(5, 10, 3), output_size=(5, 5, 5))(input_tensor)')
print('output_tensor size:', torch.nn.FractionalMaxPool3d(kernel_size=(5, 10, 3), output_size=(5, 5, 5))(input_tensor).size())
print('Task 4: Call the API torch.nn.FractionalMaxPool3d')