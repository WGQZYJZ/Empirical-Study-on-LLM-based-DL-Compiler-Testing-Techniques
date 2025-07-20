a = torch.randn(3, 3)
a = torch.randn(3, 3)
out = torch.LongTensor()
torch.nonzero(a, out=out)