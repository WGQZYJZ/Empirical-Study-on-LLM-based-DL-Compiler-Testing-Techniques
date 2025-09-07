
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.cat([x1[:, i:i+32] for i in range(0, x1.shape[1] - 96 + 32)], dim=1)


# Initializing the model
m = Model()
