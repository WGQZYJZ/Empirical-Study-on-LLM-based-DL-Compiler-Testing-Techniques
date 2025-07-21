'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
input = torch.randn(1, 1, 3, 3, requires_grad=True)
output_size = (1, 2)
import torch
input = torch.randn(1, 1, 3, 3, requires_grad=True)
output_size = (1, 2)
output = torch.nn.functional.adaptive_avg_pool2d(input, output_size)
print(output)
output.backward(torch.ones_like(output))
print(input.grad)
output = torch.nn.functional.avg_pool2d(input, kernel_size=output_size)
print(output)