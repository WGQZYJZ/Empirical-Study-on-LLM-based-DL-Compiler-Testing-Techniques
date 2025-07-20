n = 1
input = torch.randn(2, 3)
torch.special.polygamma(n, input)
n = 1
input = torch.randn(2, 3)
out = torch.zeros_like(input)
torch.special.polygamma(n, input, out=out)
n = 1
input = torch.randn(2, 3)
out = torch.zeros_like(input)
torch.special.polygamma(n, input, out=out)