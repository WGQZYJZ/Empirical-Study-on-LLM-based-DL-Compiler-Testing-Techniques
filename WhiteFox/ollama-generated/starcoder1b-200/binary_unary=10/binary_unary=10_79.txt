
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(200, 10)
 
    def forward(self, x):
        return self.linear(x) + torch.randn(1, 10).uniform_()


# Initializing the model
m = Model()


