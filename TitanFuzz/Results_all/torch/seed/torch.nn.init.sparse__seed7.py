x = torch.randn(3, 5)
torch.nn.init.sparse_(x, sparsity=0.5, std=0.01)