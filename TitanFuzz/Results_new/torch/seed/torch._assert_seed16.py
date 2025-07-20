a = torch.rand(2, 3, 4)
b = torch.rand(2, 3, 4)
torch._assert((a.shape == b.shape), 'The shape of a and b should be the same')