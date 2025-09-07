
class Model(torch.nn.Module):
    def __init__(self, embed_dim=64):
        super().__init__()
        self.layer = torch.nn.Linear(embed_dim, embed_dim)
 
    def forward(self, x1):
        return x1 * 0.5


# Initializing the model
m = Model()


