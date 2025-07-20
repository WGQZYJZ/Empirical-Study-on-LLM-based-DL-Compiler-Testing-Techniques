input = torch.rand(5, dtype=torch.float32)
other = torch.rand(5, dtype=torch.float32)
torch.logaddexp2(input, other)