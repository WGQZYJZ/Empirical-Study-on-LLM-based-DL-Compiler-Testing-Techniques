
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = self.linear(x1) + torch.zeros([]) # Here, the keyword argument "other" is omitted and the tensor 0 is added to the linear transformation result. It represents the bias parameter of the linear transformation
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3)

