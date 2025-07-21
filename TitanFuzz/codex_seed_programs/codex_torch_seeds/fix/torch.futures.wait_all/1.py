'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.futures.wait_all\ntorch.futures.wait_all(futures)\n'
import torch
t1 = torch.tensor([1, 2, 3, 4])
t2 = torch.tensor([10, 20, 30, 40])
f1 = torch.futures.Future()
f2 = torch.futures.Future()
f1.set_result(t1)
f2.set_result(t2)
print(torch.futures.wait_all([f1, f2]))
t3 = torch.tensor([100, 200, 300, 400])
f3 = torch.futures.Future()
f3.set_result(t3)
print(torch.futures.wait_all([f1, f2, f3]))