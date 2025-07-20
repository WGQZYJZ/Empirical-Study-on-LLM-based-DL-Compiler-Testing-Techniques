input = Variable(torch.Tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]]))
pool = torch.nn.MaxPool3d(kernel_size=(1, 2, 2), stride=1, padding=0)
output = pool(input)