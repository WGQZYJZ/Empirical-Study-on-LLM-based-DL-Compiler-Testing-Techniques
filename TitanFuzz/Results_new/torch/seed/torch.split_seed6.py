tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
(t1, t2) = torch.split(tensor, 2, dim=0)
(t3, t4) = torch.split(tensor, 2, dim=1)