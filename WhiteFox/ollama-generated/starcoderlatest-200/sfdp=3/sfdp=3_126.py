

# Inputs to the model
query, key, value  = torch.randn(batchsize, 8, 3, 64), torch.randn(batchsize, 32, 3, 64), torch.randn(batchsize, 32, 8, 64)
__output__  = Attention()(query, key, value)


