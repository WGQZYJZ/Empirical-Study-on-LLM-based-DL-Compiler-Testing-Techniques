
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1  = x1.permute(0, 1) 
        v2  = self.linear(v1)
        return v2

# Initializing the model
m   = Model()


# Inputs to the model
x1  = torch.randn(3, 4)

 # Run the model with an input tensor for the model that is different from the previous one.
__output__  = m(x1)
