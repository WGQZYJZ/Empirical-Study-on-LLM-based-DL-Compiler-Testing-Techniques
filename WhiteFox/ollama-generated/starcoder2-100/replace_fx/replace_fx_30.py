
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1, 0.8) # apply dropout with 0.8 probability
        v3 = torch.rand_like(v2, 5.) # generate a tensor with 5 values filled with random numbers
        return (v2 + v3).pow(2)

# Initializing the model
m  = Model()

