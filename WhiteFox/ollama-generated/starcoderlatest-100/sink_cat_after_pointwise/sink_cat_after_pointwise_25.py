
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1.view(-1), x1], dim=0)
        v2 = torch.relu(v1.permute(1,0)) # Permuting is not allowed in sink_cat_after_pointwise optimization
        v3 = self.linear(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
