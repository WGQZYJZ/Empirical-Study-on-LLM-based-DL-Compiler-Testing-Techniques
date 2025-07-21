"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.load\ntorch.hub.load(repo_or_dir, model, *args, source='github', force_reload=False, verbose=True, skip_validation=False, **kwargs)\n"
import torch
x = torch.rand(2, 3)
print(x)
model = torch.hub.load('pytorch/vision:v0.6.0', 'squeezenet1_0', pretrained=True)