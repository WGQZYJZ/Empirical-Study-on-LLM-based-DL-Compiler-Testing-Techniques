inp = torch.randn(3, 5)
torch.overrides.is_tensor_like(inp)
inp = Variable(torch.randn(3, 5))