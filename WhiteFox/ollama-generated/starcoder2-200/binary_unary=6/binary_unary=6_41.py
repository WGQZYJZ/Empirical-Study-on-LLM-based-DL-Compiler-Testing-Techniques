
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.nn.functional.linear(x1, other) - other  # 5


# Initializing the model