
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*348*3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(30, 256*348*3) # A random input tensor with shape [batch_size x embedding_dim] for the linear transformation
