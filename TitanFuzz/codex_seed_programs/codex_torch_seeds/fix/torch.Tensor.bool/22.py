'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
data = torch.tensor([[False, True], [True, False]])
print(data.bool())
'\nTask 4: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
print(data.byte())
'\nTask 5: Call the API torch.Tensor.char\ntorch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)\n'
print(data.char())
'\nTask 6: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
print(data.double())
'\nTask 7: Call the API torch.Tensor.float\ntorch.Tensor.float(_input_tensor, memory_format=torch.preserve_format)\n'
print(data.float())