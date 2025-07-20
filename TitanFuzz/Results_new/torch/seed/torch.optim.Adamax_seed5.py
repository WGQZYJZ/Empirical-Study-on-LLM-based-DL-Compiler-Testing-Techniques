x = torch.randn((1, 1), requires_grad=True)
y = torch.randn((1, 1), requires_grad=True)
optimizer = torch.optim.Adamax([x, y], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
optimizer.step()
optimizer.zero_grad()
state_dict = optimizer.state_dict()
optimizer.load_state_dict(state_dict)
param_groups = optimizer.param_groups