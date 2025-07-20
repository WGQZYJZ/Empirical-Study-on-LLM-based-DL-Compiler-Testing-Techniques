x = torch.randn(2, 3)
torch.nn.init.kaiming_uniform_(x)
x = torch.randn(2, 3)
torch.nn.init.kaiming_normal_(x)