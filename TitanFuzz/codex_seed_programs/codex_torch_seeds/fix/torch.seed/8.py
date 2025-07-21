'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
x = torch.rand(1000, 1000)
y = torch.rand(1000, 1000)
torch.seed()
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.device(0))
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(0))
torch.cuda.set_device(0)