data = torch.ones((2, 2))
torch.nn.init.sparse_(data, sparsity=0.5, std=0.01)