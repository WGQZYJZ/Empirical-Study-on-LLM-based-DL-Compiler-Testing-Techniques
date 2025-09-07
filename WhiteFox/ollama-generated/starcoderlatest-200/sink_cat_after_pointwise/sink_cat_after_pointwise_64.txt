
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        # Concatenate tensor x1 along dim=0 and tensor x2 along dim=1
        t1 = torch.cat([x1, x2], dim=0)

        # Reshape the concatenated tensor into a matrix of size 4*2
        v1 = t1.view(-1, 2)

        # Apply Tanh function on each element in v1 and return the output
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2)
x2 = torch.randn(4, 2)
