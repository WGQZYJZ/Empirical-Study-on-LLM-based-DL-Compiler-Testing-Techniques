
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 2)
 
    def forward(self, x1):
        v1 = torch.cat([x1.view(-1, 64 * 64),  # Concatenate the feature tensor with each row
                         torch.ones((x1.shape[0], 1)) * -0.7071067811865475 + 0.5], dim=-1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
