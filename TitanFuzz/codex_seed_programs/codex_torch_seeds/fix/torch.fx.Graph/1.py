'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fx.Graph\ntorch.fx.Graph(owning_module=None, tracer_cls=None)\n'
import torch
x = torch.rand(1, requires_grad=True)
y = (x * 2)
z = y.mean()
graph = torch.fx.Graph(z)
print(graph)