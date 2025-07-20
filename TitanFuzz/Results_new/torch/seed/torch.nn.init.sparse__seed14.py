input_tensor = torch.randn(3, 3)
torch.nn.init.sparse_(input_tensor, sparsity=0.5, std=0.01)