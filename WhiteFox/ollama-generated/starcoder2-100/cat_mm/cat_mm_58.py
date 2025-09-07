
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 4)
        self.linear2 = torch.nn.Linear(3, 6)

    def forward(self, x1, x2):

        v0 = torch.mm(x1, x2) 
        v1 = torch.cat([v0 for _ in range(5)], dim=0)
        return v1

# Initializing the model
m = Model()

 # Inputs to the model 
x1 = torch.randn(3, 5)
x2 = torch.randn(4, 6)
