input1 = torch.randn(100, 128)
input2 = torch.randn(100, 128)
target = torch.randn(100).ge(0).float()
output = torch.nn.functional.cosine_embedding_loss(input1, input2, target)