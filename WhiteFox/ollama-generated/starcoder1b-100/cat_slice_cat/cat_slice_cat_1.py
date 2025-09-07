
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1[:, i] for i in range(0, len(x1), self.strides)], dim=1) # List comprehension to generate the output list.
        v2 = [torch.abs(v1[i]) for i in range(len(x1))]
        return torch.stack(v2)


# Initializing the model
m = Model()


