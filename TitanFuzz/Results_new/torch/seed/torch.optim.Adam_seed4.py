params = torch.tensor([1.0, 0.0], requires_grad=True)
learning_rate = 0.001
optimizer = torch.optim.Adam([params], lr=learning_rate)
for _ in range(20):
    optimizer.zero_grad()
    loss = (((params[0] - 3) ** 2) + ((params[1] - 2) ** 2))
    loss.backward()
    optimizer.step()
    print(params)