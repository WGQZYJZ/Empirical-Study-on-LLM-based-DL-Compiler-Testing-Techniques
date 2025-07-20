x = torch.ones(2, 2, requires_grad=True)
torch.nn.init.constant_(x, 2)