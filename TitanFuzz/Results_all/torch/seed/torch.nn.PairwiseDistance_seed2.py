input1 = Variable(torch.randn(2, 3))
input2 = Variable(torch.randn(2, 3))
output = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)(input1, input2)