
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v7 = torch.cat([x1, x3], dim=1) # Concatenate input tensors along dimension 1
        return v7


# Initializing the model