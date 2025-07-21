'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_shapes\ntorch.broadcast_shapes(*shapes)\n'
import torch
inputs = [torch.randn(1, 3, 224, 224), torch.randn(1, 3, 224, 224)]
shapes = torch.broadcast_shapes(*[i.shape for i in inputs])
print(shapes)