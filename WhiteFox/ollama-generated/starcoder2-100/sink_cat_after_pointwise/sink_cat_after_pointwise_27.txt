
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        return torch.cat([
            torch.tensor([[1., 2], [3., 4]]), 
            torch.tensor([[5., 6], [7., 8]]), 
        ], dim=0).view(-1)

# Initializing the model