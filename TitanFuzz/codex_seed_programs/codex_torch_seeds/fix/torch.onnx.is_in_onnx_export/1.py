'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.onnx.is_in_onnx_export\ntorch.onnx.is_in_onnx_export()\n'
import torch
x = torch.randn(3, 4)
y = torch.randn(3, 4)
z = torch.randn(3, 4, 5)
torch.onnx.is_in_onnx_export()