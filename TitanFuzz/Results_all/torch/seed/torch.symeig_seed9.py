input = torch.randn(3, 3)
input = (input + input.t())
(e_val, e_vec) = torch.symeig(input, eigenvectors=True, upper=False)
e_val = torch.symeig(input, eigenvectors=False, upper=False)