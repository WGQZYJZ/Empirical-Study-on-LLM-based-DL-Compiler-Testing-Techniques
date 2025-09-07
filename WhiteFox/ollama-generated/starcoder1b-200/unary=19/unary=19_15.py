
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 8 * 8, 1)
 
    def forward(self, x1):
        v1 = x1.view(-1, 32 * 8 * 8)  # Flatten the input tensor
        v2 = self.linear(v1)  # Apply a linear transformation to the input tensor
        return torch.sigmoid(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32 * 8 * 8)
