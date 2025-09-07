
class Model(torch.nn.Module):
    def __init__(self, embed_dim=32):
        super().__init__()
        self.conv = torch.nn.Conv1d(3, embed_dim, 1)
 
    def forward(self, x1):
        x2 = self.conv(x1).float()
        return x2


# Initializing the model
m = Model()


