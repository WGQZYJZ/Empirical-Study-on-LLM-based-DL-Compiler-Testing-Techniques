input = torch.randn(3, 4, requires_grad=True)
end = torch.randn(3, 4, requires_grad=True)
weight = torch.randn(3, 4, requires_grad=True)
output = torch.lerp(input, end, weight)