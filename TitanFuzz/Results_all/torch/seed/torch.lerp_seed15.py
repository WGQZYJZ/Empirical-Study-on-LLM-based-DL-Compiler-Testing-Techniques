input = torch.randn(5, 3)
end = torch.randn(5, 3)
weight = torch.rand(5, 3)
torch.lerp(input, end, weight)