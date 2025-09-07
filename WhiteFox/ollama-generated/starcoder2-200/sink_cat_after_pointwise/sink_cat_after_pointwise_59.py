
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()

    def forward(self, input):
        t1  = torch.cat([input, input], 2)
        return torch.relu(t1.view(-1, 4).view(30)).sum()


# Initializing the model with `dim=1`
m  = Model(dim=1)

# Inputs to the model: shape of the 2 tensors must be 60 x 8.
x1  = torch.randn(60, 4*8) # Shape of this tensor should not matter

 