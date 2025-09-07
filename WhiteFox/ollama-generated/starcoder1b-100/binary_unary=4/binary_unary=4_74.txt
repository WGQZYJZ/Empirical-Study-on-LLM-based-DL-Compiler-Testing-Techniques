
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        v2 = v1 + kwargs['other']
        return self.relu(v2)


# Initializing the model
m = Model(torch.randn(4))


