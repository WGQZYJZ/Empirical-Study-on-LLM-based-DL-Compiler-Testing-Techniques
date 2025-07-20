tensor = torch.randn(4, 4)
torch.nn.init.sparse_(tensor, sparsity=0.5, std=0.01)