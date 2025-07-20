x = Variable(torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
y = Variable(torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
torch.nn.functional.leaky_relu(x, negative_slope=0.01, inplace=False)
torch.nn.functional.leaky_relu(x, negative_slope=0.01, inplace=True)