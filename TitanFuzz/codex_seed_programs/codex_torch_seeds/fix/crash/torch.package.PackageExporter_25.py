'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.package.PackageExporter\n'
import torch
data = torch.randn(2, 3)
print(data)
torch.package.PackageExporter(data, './test_package.zip')