
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        # Trigger sink_cat_after_pointwise optimization here
        v2 = v1.view(-1, 4, 3)
        t3 = torch.relu(v2)
        return t3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 1, 3, 4)
x2 = torch.randn(2, 10, 6, 7)
