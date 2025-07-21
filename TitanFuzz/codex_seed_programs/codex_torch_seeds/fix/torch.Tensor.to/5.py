'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, *args, **kwargs)\n'
import torch
device = torch.device(('cuda:0' if torch.cuda.is_available() else 'cpu'))
input_tensor = torch.rand(1, 3, 224, 224)
torch.Tensor.to(input_tensor, device)