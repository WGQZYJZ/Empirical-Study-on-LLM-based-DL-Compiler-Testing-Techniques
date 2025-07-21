'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logaddexp\ntorch.Tensor.logaddexp(_input_tensor, other)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('CUDA available: ', torch.cuda.is_available())
print('cuDNN enabled: ', torch.backends.cudnn.enabled)
print('\nTask 2: Generate input data')
input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
print('input_tensor: ', input_tensor)
print('other: ', other)
print('\nTask 3: Call the API torch.Tensor.logaddexp')
print('torch.Tensor.logaddexp(input_tensor, other) = ', torch.Tensor.logaddexp(input_tensor, other))