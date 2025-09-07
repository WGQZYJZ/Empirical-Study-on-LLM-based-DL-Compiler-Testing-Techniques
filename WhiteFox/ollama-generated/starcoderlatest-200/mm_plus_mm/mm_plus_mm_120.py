
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(128, 3)

    def forward(self, x1):
        v1 = torch.mm(x1, x1) # Input 1 times itself, input 2 times itself
        v2 = torch.mm(x1, x1) # Input 3 times itself
        v3 = v1 + v2 
        return self.mm(v3)


# Initializing the model
m = Model()


