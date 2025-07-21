import torch
input = torch.randn(1, 1, 3, 3, 3)
output = torch.nn.functional.avg_pool3d(input, kernel_size=3, stride=1, padding=0)