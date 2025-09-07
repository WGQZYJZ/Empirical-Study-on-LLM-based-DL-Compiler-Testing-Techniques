
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        negative_slope = 0.2
        v2 = torch.where(v1 > 0, v1, negative_slope * v1) # Apply the leaky ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 10, batch_size=8)
