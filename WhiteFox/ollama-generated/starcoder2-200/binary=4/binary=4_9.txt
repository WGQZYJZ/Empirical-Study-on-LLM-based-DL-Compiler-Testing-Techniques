
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + torch.randn_like(v1) # Here we use a random tensor to illustrate the case when 'other' is not specified in the torch.nn.Linear function.
        return v2
# Initializing the model:
m = Model()


# Inputs to the model:
x1  = torch.randn(4, 3) # Note that we set a batch size of 4 and 3 feature channels for our input tensor.
__output__  = m(x1)

