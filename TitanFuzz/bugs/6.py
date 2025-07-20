import torch

input1 = torch.randn(1, 1, 2, 2, requires_grad=True).cuda()
weight1 = torch.randn(1, 1, 2, 2, requires_grad=True).cuda()
output1 = torch.nn.functional.conv_transpose2d(input1, weight1, stride=2, padding=2)
print(output1)

input2 = torch.randn(1, 1, 2, 2, requires_grad=True)
weight2 = torch.randn(1, 1, 2, 2, requires_grad=True)
output2 = torch.nn.functional.conv_transpose2d(input2, weight2, stride=2, padding=2)

