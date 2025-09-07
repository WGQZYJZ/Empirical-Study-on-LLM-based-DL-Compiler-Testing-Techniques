

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, y1=0):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v4  = v1 -y1  # Subtract 'other' from the output of the linear transformation
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x2 = torch.randn(2, 3)
y2 = np.array([1., 0.5])

