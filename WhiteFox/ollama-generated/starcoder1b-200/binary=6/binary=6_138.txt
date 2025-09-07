
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 0.5  # Apply the linear transformation to the input tensor
        return v1


# Initializing the model
m = Model(-0.25)


