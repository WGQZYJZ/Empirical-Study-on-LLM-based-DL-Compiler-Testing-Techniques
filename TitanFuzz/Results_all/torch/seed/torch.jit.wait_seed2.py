x = torch.zeros(1)
future = torch.jit._fork(torch.add, x, 1)
torch.jit.wait(future)