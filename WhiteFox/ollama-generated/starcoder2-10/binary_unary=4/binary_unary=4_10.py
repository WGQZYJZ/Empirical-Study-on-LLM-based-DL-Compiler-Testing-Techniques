

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):  # Input tensor 1 has to be named `x1`, while input tensor 2 should have a name other than 'y2'. Otherwise, the model will fail.
        v1 = torch.nn.Linear()(x1) 
        v3 = v1 + y2  # Another tensor was added to the output of the linear transformation. The name of another tensor is `y2`.
        v4 = torch.relu(v3)  
        return v4

# Initializing the model with the keyword argument set:
m  = Model()


# Inputs to the model, using keyword arguments to override the default argument names (for this example x1 and y2).
__x1__, __y2__ = torch.randn(3, 8), torch.randn(4)

