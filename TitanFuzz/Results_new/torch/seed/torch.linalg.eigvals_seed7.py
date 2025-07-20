A = Variable(torch.Tensor([[1, 2], [3, 4]]), requires_grad=False)
eigvals = torch.linalg.eigvals(A)