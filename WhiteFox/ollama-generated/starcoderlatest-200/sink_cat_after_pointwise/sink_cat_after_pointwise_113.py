
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=0) # A Concat op is inserted after the linear function in this model
        t3 = torch.relu(v1) # Apply relu to the reshaped tensor
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, requires_grad=True)
x2 = x1.permute(0, 2, 1)
