
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=64):
        super().__init__()
        self.dense1 = torch.nn.Linear(hidden_dim, hidden_dim)
        self.dense2 = torch.nn.Linear(hidden_dim, hidden_dim)
 
    def forward(self, x1, x2):
        # Use the input tensor for both linear layers, then add a third linear layer to get the output
        v  = torch.cat((x1, x2), dim=1)
        v  = self.dense1(v) + self.dense2(v)
        return v


# Initializing the model
m = Model()


# Inputs to the model
h1 = torch.randn(64, 3)
