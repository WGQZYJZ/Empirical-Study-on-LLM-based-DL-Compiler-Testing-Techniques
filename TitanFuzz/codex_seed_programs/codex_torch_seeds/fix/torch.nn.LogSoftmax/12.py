'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
input = torch.randn(2, 3, requires_grad=True)
print(input)
output = torch.nn.LogSoftmax(dim=1)(input)
print(output)
output_expected = torch.log_softmax(input, dim=1)
print(output_expected)
print(output.grad_fn)
print(output_expected.grad_fn)