'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix_\ntorch.Tensor.fix_(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=255, size=(1, 3, 224, 224), dtype=torch.float)
torch.Tensor.fix_(_input_tensor)