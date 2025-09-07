
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(24,1)

    def forward(self,x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        return v2

# Initializing the model
m  = Model()


# Inputs to the model (other is a dummy value for demonstration purpose only.)
x1 = torch.randn(4, 24)
other  = torch.tensor([0], dtype=torch.double) # Dummy value in PyTorch
