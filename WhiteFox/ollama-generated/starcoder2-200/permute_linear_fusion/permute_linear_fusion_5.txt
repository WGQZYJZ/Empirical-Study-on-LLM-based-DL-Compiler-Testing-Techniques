
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3  = x1.permute(0, 2, 1).view(-1) 
        v4  = self.linear(v3)
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1   = torch.randn(1, 2, 2)

