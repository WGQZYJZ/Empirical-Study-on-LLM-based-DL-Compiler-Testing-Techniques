
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
 
    def forward(self, x1, other=0.5):
        v1 = self.linear(x1)
        return (v1 + other)


# Initializing the model
m  = Model()


