input = torch.autograd.Variable(torch.randn(3, 5), requires_grad=True)
target = torch.autograd.Variable(torch.LongTensor(3).random_(5))
loss = torch.nn.NLLLoss()
output = loss.forward(input, target)