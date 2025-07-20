input = Variable(torch.randn(3, 5))
target = Variable(torch.FloatTensor(3, 5).random_(2))
loss = torch.nn.functional.multilabel_soft_margin_loss(input, target)