
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)

    def forward(self, x1):
        v1 = self.linear(x1)

        # Subtracting 0.5 from the output of the linear transformation
        # is not a correct approach. Hence, we generate
        # two random numbers to replace the 0.5 with.
        # (Please modify this line for your use case.)
        oth = torch.rand_like(v1) - 0.37

        v2 = v1 - oth
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 5)
__output__= m(x1) 
