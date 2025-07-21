'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.modules.module.register_module_backward_hook\ntorch.nn.modules.module.register_module_backward_hook(hook)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
torch.nn.modules.module.register_module_backward_hook(x)
print(x)