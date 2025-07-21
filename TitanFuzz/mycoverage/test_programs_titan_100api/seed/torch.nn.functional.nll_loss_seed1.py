input_data = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.LongTensor(3).random_(5))
loss = torch.nn.functional.nll_loss(input_data, target)