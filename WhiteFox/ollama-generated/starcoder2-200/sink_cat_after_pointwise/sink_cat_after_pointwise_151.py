
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1 + 100.0 * x2]) 
        return v.view(-1).relu() # -1 means that it should be inferred as the batch size automatically


# Initializing the model