A = Variable(torch.randn(4, 4), requires_grad=True)
B = torch.linalg.matrix_norm(A)
B.backward()