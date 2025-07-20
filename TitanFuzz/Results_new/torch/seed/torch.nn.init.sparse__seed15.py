tensor = torch.randn(2, 3)
torch.nn.init.sparse_(tensor, sparsity=0.5)