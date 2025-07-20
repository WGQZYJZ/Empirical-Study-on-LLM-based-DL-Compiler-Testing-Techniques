data = torch.randn(2, 2)
target = torch.randn(2)
optimizer = torch.optim.Adam([data], lr=0.1)
optimizer.step()