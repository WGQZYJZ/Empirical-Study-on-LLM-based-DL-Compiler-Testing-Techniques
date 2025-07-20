input = torch.randn(3, 3)
input = (input + input.t())
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)