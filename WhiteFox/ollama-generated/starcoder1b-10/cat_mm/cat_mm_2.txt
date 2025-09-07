
class Model(torch.nn.Module):
    def __init__(self, n_features):
        super().__init__()
        self.fc1 = torch.nn.Linear(n_features * 2 + 10, 4)
        self.fc2 = torch.nn.Linear(4, 4)

    def forward(self, x):
        v1 = torch.cat([x[:, :], x[:, -1:]], dim=-1) # Concatenation of the result tensor along a specified dimension
        v2 = v1 @ v1.t() # Apply matrix multiplication to compute the second part of the concatenation
        return self.fc2(self.fc1(v2))


# Initializing the model
m = Model(3)


# Inputs to the model
x = torch.randn(1, 4, 10)
