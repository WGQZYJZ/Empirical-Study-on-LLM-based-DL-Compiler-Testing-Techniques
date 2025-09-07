
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=0)  # Concatenate tensors along a dimension and then apply view
        return v.view(-1, x1.shape[-1])


# Initializing the model
m  = Model()


# Inputs to the model