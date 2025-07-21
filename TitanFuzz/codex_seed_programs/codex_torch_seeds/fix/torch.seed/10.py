'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
input_data = torch.randn(1, 1, 32, 32)
torch.seed()
torch.cuda.manual_seed(0)
torch.cuda.manual_seed_all(0)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.enabled = False