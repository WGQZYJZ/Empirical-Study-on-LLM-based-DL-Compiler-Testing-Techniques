'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor)
output_tensor = input_tensor.type(torch.FloatTensor)
print(output_tensor)
output_tensor = input_tensor.type(torch.IntTensor)
print(output_tensor)
output_tensor = input_tensor.type(torch.DoubleTensor)
print(output_tensor)
output_tensor = input_tensor.type(torch.LongTensor)
print(output_tensor)