
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.relu(x1)  # pointwise
        x3 = torch.cat([
            torch.rand((4, 8)), 
            self._conv_layer(torch.randn((64, 30))),
        ], dim=0).view(-1, 512).detach()  
        # concatenate along the first dimension 
        return torch.relu(x3)

# Initializing the model
m = Model()

