
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.full([x1.shape[0], x1.shape[2]], 1, device=x1.device)


# Initializing the model
m = Model()


# Inputs to the model
t = torch.randn(3, 4)
