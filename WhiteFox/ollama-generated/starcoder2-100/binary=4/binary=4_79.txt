
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v0 = other # add an additional tensor to the output of a linear transformation after this line 
        return self.linear(x1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 32)
__output__  = m(x1)

# Additional tensors
other = torch.randn([2, 64])
