
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.cat([x1[:, i:i+9] for i in range(0, len(x1), 9)], dim=1)


# Initializing the model
m = Model()


