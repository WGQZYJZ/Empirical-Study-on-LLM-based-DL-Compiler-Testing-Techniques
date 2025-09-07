
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10,2)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        if not other:
            return v1 + v1 * 3
        else:
            return v1 + other


# Initializing the model
m  = Model()

 # Inputs to the model
 x2  = torch.randn(5, 8096, dtype=torch.double)
 
# Keyword argument for the model
other_tensor = torch.randn([1], 8096, dtype=torch.double)

# Applying the model with keyword argument to generate a new tensor and passing it as an argument to the `forward` method of the model (this will make it different from previous model). Also apply the model without the keyword argument.
__output1__ = m(x2, other_tensor)  # Model call with keyword argument
__output2__ = m(x2)  # Model call without keyword argument

