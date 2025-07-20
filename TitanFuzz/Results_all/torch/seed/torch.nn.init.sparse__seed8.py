input_data = torch.randn(3, 5)
torch.nn.init.sparse_(input_data, sparsity=0.5)