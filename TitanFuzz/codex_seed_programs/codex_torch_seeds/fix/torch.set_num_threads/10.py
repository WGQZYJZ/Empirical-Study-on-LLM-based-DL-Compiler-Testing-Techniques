'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
import time
input_data = torch.randn(1000, 1000)
torch.set_num_threads(2)
start_time = time.time()
for i in range(100):
    torch.mm(input_data, input_data)
end_time = time.time()
print('Time cost: ', (end_time - start_time))