input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.FloatTensor(3, 5).random_(2))
loss = torch.nn.functional.binary_cross_entropy_with_logits(input, target)