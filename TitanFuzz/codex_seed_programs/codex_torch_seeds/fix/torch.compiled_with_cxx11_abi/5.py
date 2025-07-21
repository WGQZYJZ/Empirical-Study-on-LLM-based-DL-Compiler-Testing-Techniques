'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.compiled_with_cxx11_abi\ntorch.compiled_with_cxx11_abi()\n'
import torch
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
y = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
print(torch.compiled_with_cxx11_abi())
print(torch.cuda.is_available())
print(torch.cuda.current_device())
print(torch.cuda.device_count())