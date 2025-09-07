
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)

    def forward(self, x):
        t1 = torch.cat([x[:, :, :], x[:, :, :]], dim=-1) # Concatenate tensors along a dimension -1
        t2 = t1.view(-1, self.linear1.in_features) # Reshape the concatenated tensor
        return self.linear1(t2)

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 4, 2)
