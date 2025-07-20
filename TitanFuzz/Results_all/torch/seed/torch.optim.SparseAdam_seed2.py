input_data = torch.randn(100, 10)
target = torch.randint(0, 10, (100,))
optimizer = torch.optim.SparseAdam(params=nn.Linear(10, 10).parameters(), lr=0.1)
for _ in range(100):
    optimizer.zero_grad()
    loss = nn.functional.cross_entropy(nn.Linear(10, 10)(input_data), target)
    loss.backward()
    optimizer.step()
    print(loss.item())