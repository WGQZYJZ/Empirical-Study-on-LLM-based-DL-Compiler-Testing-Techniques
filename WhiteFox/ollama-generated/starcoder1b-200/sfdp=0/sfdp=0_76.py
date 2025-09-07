
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 4)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1, x2):
        w1  = self.linear(x1)
        w2  = self.linear(x2)
        w3  = torch.matmul(w1, w2.transpose(-1, -2))
        v1  = self.sigmoid(w3)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 4)
x2 = torch.randn(10, 5)
