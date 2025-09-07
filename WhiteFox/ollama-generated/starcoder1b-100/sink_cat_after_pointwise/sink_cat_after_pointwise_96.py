
class Model(torch.nn.Module):
    def __init__(self, config, **kwargs):
        super().__init__()

    def forward(self, x1, x2, **kwargs):  # In the model, `x1`, `x2` are concatenated
        v1 = torch.cat([tensor1, tensor2, ...], dim=...)
        v2 = t1.view(...)  # Reshape v1
        return torch.relu(v2)


# Initializing the model
m = Model()

