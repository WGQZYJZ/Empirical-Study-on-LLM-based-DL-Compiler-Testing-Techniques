start = torch.randn(4, 4)
end = torch.randn(4, 4)
weight = torch.rand(4, 4)
output = torch.lerp(start, end, weight)