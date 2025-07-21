'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fx.Graph\ntorch.fx.Graph(owning_module=None, tracer_cls=None)\n'
import torch
x = torch.randn(1, 2, 3, 4)
y = torch.randn(5, 6)
graph = torch.fx.Graph(x, y)
print(graph)