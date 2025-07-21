'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sparse_mask\ntorch.Tensor.sparse_mask(_input_tensor, mask)\n'
import torch
import torch
input_tensor = torch.randn(3, 4)
print('input_tensor:', input_tensor)
mask = torch.tensor([[True, True, True, True], [False, True, True, True], [True, False, True, True]], dtype=torch.bool)
print('mask:', mask)
result = input_tensor.sparse_mask(mask)
print('result:', result)