
class Model(torch.nn.Module):
    def __init__(self, n_output, n_feature):
        super().__init__()
        self.linear1 = torch.nn.Linear(n_feature, 40)
        self.linear2 = torch.nn.Linear(40, n_output)

    def forward(self, x1):
        # Input tensor
        x2 = self.linear1(x1)

        # Concatenate along the dimension 'dim' and return the result as a flattened vector
        v  = torch.cat([x2, torch.zeros((x2.shape[0], 1))], dim=-1)
        return self.linear2(v)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(10, 2, 64, 64)
