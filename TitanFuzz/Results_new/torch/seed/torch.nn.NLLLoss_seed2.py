x = torch.randn(3, requires_grad=True)
y = torch.tensor([1, 0, 3], dtype=torch.int64)
loss = torch.nn.NLLLoss()
output = loss(torch.log_softmax(x, dim=0), y)
output.backward()
x = torch.rand