input = torch.rand(3, 3, requires_grad=True)
output = torch.special.entr(input)