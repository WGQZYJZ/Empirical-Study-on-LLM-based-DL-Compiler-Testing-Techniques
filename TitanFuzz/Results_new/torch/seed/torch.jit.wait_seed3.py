x = torch.tensor([1, 2, 3])
future = torch.jit._fork(torch.add, x, x)
torch.jit.wait(future)