'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
x = torch.rand(5000, 5000)
y = torch.rand(5000, 5000)
torch.set_num_threads(4)
start = time.time()
z = torch.mm(x, y)
end = time.time()
print('time: {} sec'.format((end - start)))
print(z)