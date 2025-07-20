torch.set_num_interop_threads(4)
torch.set_num_threads(4)
x = torch.tensor([[1, 2], [3, 4]])
y = torch.matmul(x, x)