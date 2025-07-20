start = torch.rand(3, 3)
end = torch.rand(3, 3)
weight = torch.rand(3, 3)
output = torch.lerp(start, end, weight)