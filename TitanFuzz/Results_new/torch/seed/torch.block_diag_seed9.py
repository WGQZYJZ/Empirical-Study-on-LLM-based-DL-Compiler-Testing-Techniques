t1 = torch.rand(3, 3)
t2 = torch.rand(4, 4)
t3 = torch.rand(5, 5)
t4 = torch.block_diag(t1, t2, t3)