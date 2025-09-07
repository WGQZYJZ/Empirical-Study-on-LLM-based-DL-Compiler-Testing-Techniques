
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0) # concatenate along the dimension of batch size
        v1 = t1.view(-1) # reshape to 1-dim tensor
        v2 = torch.relu(v1) # apply pointwise unary operation (like ReLU or Tanh)
        return self.linear(v2)


# Inputs to the model
x1 = torch.randn(4, 1, 50) # batch_size x 1-dim tensor with shape [batch size, max input length]
x2 = torch.randn(4, 3, 50) # batch_size x 1-dim tensor with shape [batch size, input dimension]
