"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.load\ntorch.hub.load(repo_or_dir, model, *args, source='github', force_reload=False, verbose=True, skip_validation=False, **kwargs)\n"
import torch
input_data = torch.randn(1, 3, 224, 224)
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet50', pretrained=True)
model.eval()
with torch.no_grad():
    output = model(input_data)
print(output[0])
print(torch.argmax(output[0]).item())