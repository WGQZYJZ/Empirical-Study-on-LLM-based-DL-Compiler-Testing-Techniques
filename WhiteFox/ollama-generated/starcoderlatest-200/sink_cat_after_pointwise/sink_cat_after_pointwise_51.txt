
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1) # concat inputs along the second dimension
        t2 = t1.view(-1, 4)        # reshape to a flat tensor of size (N*4,)
        t3 = torch.relu(t2)       # apply Relu to this flattened tensor
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
