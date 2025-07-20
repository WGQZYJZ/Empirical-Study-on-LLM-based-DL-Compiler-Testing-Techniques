input1 = Variable(torch.randn(100, 128))
input2 = Variable(torch.randn(100, 128))
target = Variable(torch.FloatTensor(100).random_(0, 2))
output = torch.nn.functional.cosine_embedding_loss(input1, input2, target)