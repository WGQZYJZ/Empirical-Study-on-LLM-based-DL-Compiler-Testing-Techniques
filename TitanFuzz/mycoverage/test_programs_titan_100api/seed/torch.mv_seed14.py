input = torch.randn(2, 3)
vec = torch.randn(3)
torch.mv(input, vec)
torch.mm(input, vec.view(3, 1))