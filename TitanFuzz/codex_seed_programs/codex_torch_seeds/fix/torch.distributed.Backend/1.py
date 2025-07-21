'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.Backend\ntorch.distributed.Backend(name)\n'
import torch
import torch.distributed as dist
x = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], requires_grad=True)
y = torch.tensor([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], requires_grad=True)
backend = dist.Backend('gloo')
print('The backend handle is: {}'.format(backend))
print('The type of backend handle is: {}'.format(type(backend)))