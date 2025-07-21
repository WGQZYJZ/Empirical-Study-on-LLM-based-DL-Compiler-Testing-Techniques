'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.initial_seed\ntorch.initial_seed()\n'
import torch
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
torch.initial_seed()
torch.cuda.manual_seed(seed=10)
torch.cuda.manual_seed_all(seed=10)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False