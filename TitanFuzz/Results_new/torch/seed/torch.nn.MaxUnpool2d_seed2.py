dtype = torch.FloatTensor
(N, C, H, W) = (2, 3, 4, 4)
x = Variable(torch.randn(N, C, H, W).type(dtype), requires_grad=True)
indices = Variable(torch.LongTensor([0, 2, 2, 2, 1, 1, 1, 1]).view(2, 2, 2))
pool = torch.nn.MaxPool2d(2, stride=2, return_indices=True)
unpool = torch.nn.MaxUnpool2d(2, stride=2)
(y, indices) = pool(x)
x_hat = unpool(y, indices)