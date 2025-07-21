"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.load\ntorch.hub.load(repo_or_dir, model, *args, source='github', force_reload=False, verbose=True, skip_validation=False, **kwargs)\n"
import torch
input_data = torch.randn(20, 3, 32, 32)
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()
device = torch.device(('cuda' if torch.cuda.is_available() else 'cpu'))
model = model.to(device)
input_data = input_data.to(device)
output = model(input_data)
print(output.shape)