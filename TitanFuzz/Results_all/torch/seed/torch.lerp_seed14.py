input = torch.randn(4, 1, requires_grad=True)
end = torch.randn(4, 1, requires_grad=True)
weight = torch.randn(4, 1, requires_grad=True)
output = torch.lerp(input, end, weight)