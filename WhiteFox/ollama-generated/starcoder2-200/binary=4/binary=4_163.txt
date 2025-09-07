
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2560*3*19*19, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor

# Initializing the model
m  = Model()


# Inputs to the model