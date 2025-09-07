
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.cat(input_tensors, dim=1)
        w = v[:, 0:size]
        z = torch.cat([v, w], dim=1)
        return z


# Initializing the model
m = Model()


