t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([1.0, 2.0, 3.0])
t3 = torch.promote_types(t1.dtype, t2.dtype)
t4 = torch.promote_types(t2.dtype, t1.dtype)