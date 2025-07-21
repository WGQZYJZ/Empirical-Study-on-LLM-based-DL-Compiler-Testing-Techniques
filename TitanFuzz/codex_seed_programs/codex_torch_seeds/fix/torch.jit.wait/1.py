'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.wait\ntorch.jit.wait(future)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
future = torch.jit._fork(torch.sum, input_data)
torch.jit.wait(future)
print(future.value())