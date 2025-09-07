
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # Flatten the output of a convolutional layer to (N, C) for the linear transformation 
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
