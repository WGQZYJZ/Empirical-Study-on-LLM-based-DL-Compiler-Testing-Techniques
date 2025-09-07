
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 16)

    def forward(self, x): 
        v0=x
        v1=v0
        v7=self.linear(v1)
        v9=torch.tanh(v7)
        return v9

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(2, 32)
