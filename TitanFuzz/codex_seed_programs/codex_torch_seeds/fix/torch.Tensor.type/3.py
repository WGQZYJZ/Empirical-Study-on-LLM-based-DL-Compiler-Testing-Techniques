'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor: ', input_tensor)
print('input_tensor.type: ', input_tensor.type())
print('input_tensor.type(torch.DoubleTensor): ', input_tensor.type(torch.DoubleTensor))
print('input_tensor.type(torch.FloatTensor): ', input_tensor.type(torch.FloatTensor))
print('input_tensor.type(torch.LongTensor): ', input_tensor.type(torch.LongTensor))
print('input_tensor.type(torch.ByteTensor): ', input_tensor.type(torch.ByteTensor))
print('input_tensor.type(torch.CharTensor): ', input_tensor.type(torch.CharTensor))
print('input_tensor.type(torch.ShortTensor): ', input_tensor.type(torch.ShortTensor))