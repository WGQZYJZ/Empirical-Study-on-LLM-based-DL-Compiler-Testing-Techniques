'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.initial_seed\ntorch.initial_seed()\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.initial_seed()
torch.cuda.initial_seed()
torch.cuda.manual_seed(10)
torch.cuda.manual_seed_all(10)