input = torch.randn(3, 3)
(eig_val, eig_vec) = torch.eig(input, True)
eig_val = torch.eig(input, False)