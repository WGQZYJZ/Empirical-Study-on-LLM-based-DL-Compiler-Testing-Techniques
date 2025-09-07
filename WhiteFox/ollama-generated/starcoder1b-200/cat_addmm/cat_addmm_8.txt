
class Model(torch.nn.Module):
    def __init__(self, input_dim=3):
        super().__init__()
        self.input = torch.nn.Linear(input_dim, 8)
 
    def forward(self, x1):
        v1 = self.input(x1)
        v2 = torch.addmm(v1, x1, x1.t())
        return v2


# Initializing the model
m = Model()

