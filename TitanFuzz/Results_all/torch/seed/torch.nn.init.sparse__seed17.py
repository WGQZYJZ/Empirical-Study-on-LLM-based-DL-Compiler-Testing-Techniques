input_data = torch.randn(2, 3)
torch.nn.init.sparse_(input_data, sparsity=0.5, std=0.1)