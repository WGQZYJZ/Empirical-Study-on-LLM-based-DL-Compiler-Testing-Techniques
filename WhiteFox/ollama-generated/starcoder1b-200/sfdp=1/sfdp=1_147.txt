
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear = torch.nn.Linear(dim, dim)
 
    def forward(self, x):
        x = x + 1e-8
        x = F.leaky_relu(self.linear(x), negative_slope=0.3)
        return x


# Initializing the model
m = Model(4)


# Inputs to the model
query  = torch.randn(2, 4)
key    = torch.randn(2, 4)
value  = torch.randn(2, 5)
