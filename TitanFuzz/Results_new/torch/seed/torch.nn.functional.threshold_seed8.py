x = Variable(torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8]]))
y = torch.nn.functional.threshold(x, threshold=3, value=0)