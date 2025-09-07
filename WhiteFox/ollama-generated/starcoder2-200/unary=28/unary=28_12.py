
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=-1e-4):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 5)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = torch.clamp_min(v1, min_value=0.)
        v3  = torch.clamp_max(v2, max_value=-1e-4)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(64, 28*28)


# Running the model without the clamping
out0  = m(x) # Output after running the model with no argument

# Running the model with the clamping of -1e-4 as max_value and 0 as min_value.
out  = m(x, min_value=0., max_value=-1e-4)

