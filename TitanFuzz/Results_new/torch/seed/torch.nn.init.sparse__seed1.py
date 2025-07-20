tensor = torch.empty(2, 2)
torch.nn.init.sparse_(tensor, sparsity=0.5)
tensor = torch.empty(2, 2)
torch.nn.init.xavier_normal_(tensor)