t1 = torch.tensor([[1, 2], [3, 4]])
t2 = torch.tensor([[9], [10]])
t3 = torch.broadcast_tensors(t1, t2)