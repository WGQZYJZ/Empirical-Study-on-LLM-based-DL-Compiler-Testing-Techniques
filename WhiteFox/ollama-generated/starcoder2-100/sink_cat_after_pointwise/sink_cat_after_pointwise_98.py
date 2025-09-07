
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # type: ignore[override]
        v1 = torch.cat([x1], dim=2)
        v2 = v1.view(-1, 3, 4).relu()
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.ones(100, 5) # 100 samples of 5-dimension 5D tensors.
