
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3  = torch.cat([x1, x2], dim=0) 
        v4 = v3.view(-1, ...) # -1 is an indication to PyTorch to infer the correct value of the first dimension
        v5  = torch.relu(v4)

        return v5


# Initializing the model
m = Model()
