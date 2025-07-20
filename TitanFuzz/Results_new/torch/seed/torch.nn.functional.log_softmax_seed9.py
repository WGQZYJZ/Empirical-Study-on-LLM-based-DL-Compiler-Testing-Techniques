x = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]], dtype=torch.float32)
y = torch.nn.functional.log_softmax(x, dim=1)
x_sum = torch.sum(torch.exp(x), dim=1)
y_sum = torch.sum(torch.exp(y), dim=1)