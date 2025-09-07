
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(32, 64)
        self.layer2 = torch.nn.Linear(64, 64)
 
    def forward(self, x):
        v1 = x.matmul(x).matmul(torch.ones_like(x)) + 3
        v2 = torch.softmax(v1 / 5., dim=-1) * v1
        return self.layer1(v2), self.layer2(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 8) # size: (N x H x W x C)
