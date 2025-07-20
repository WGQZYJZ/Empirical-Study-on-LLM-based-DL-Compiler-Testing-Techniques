input = torch.randn(3, 3)
input = (input.t() @ input)
(eigenvalues, eigenvectors) = torch.symeig(input, eigenvectors=True)