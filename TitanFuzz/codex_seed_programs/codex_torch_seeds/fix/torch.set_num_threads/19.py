'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
torch.set_num_threads(2)
x = torch.rand(5000, 5000)
y = torch.rand(5000, 5000)
start_time = time.time()
for i in range(10):
    res = torch.mm(x, y)
print(('--- %s seconds ---' % (time.time() - start_time)))