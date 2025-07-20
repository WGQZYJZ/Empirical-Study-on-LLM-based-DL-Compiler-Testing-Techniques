A = Variable(torch.randn(2, 2), requires_grad=True)
slogdet = torch.linalg.slogdet(A)