
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = relu(t1)
        return t2


# Initializing the model
m = Model()


