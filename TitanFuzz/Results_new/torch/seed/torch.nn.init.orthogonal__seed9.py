input_tensor = torch.rand(2, 3)
torch.nn.init.orthogonal_(input_tensor)
input_tensor = torch.rand(2, 3)
torch.nn.init.sparse_(input_tensor, sparsity=0.5)