
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        return relu(v1 + other)


# Initializing the model and setting keyword argument `other` for class `Model`
m  = Model()
m.forward(torch.randn(1,64))


