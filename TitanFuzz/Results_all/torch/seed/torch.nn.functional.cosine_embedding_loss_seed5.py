input1 = Variable(torch.randn(100, 128))
input2 = Variable(torch.randn(100, 128))
target = Variable(torch.Tensor(100).random_(2))
loss = torch.nn.functional.cosine_embedding_loss(input1, input2, target)