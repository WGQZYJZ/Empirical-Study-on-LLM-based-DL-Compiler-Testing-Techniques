input = torch.randn(4, 4)
end = torch.randn(4, 4)
weight = torch.randn(4, 4)
result = torch.lerp(input, end, weight)