
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.Linear(32,8)(x1)
        v2  = v1 + other  # Please add this argument.
        v3  = torch.nn.functional.relu(v2)
        return v3


# Initializing the model