'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.onnx.is_in_onnx_export\ntorch.onnx.is_in_onnx_export()\n'
import torch
from torch.autograd import Variable
from torch.onnx import OperatorExportTypes
import torch
x = Variable(torch.randn(1, 3, 224, 224))
torch.onnx.is_in_onnx_export()
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.onnx.export\ntorch.onnx.export(model, x, "resnet18.onnx", verbose=True)\n'
import torch
from torch.autograd import Variable
from torch.onnx import OperatorExportTypes
import torch
x = Variable(torch.randn(1, 3, 224, 224))
torch