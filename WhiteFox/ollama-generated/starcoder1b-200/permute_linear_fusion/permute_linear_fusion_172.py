
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return t1[0] * t2[0]

 # Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
