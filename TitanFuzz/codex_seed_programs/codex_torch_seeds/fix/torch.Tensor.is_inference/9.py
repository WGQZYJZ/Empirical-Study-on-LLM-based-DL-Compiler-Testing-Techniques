'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_inference\ntorch.Tensor.is_inference(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224, dtype=torch.float32, device='cuda')
torch.Tensor.is_inference(input_tensor)