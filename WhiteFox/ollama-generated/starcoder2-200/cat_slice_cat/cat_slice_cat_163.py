
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.cat([x1[:, 0:9223372036854775807], x1[:, -size:], dim=1])


# Initializing the model