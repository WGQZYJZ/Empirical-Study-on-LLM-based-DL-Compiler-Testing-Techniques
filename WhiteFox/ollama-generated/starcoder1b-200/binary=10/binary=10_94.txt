
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 8)
 
    def forward(self, x1, other=None):
        # Pass the input tensor to the linear transformation
        v1 = self.linear(x1)
 
        # Add another input tensor to the output of the linear transformation
        if not other is None:
            return (v1 + other) * 0.5
        else:
            return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
other = torch.randn(1, 8)
