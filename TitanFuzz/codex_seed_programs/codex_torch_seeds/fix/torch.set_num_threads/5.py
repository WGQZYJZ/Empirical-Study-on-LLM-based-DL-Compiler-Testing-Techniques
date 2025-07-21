'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
x = torch.ones(2, 2)
y = torch.ones(2, 2)
torch.set_num_threads(4)
start = time.time()
for i in range(100):
    z = (x + y)
end = time.time()
print('Time: ', (end - start))