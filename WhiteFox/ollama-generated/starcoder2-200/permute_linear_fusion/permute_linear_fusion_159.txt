

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn([30]) # generate a random vector
        v2  = torch.tensor([50]) # generate another vector of size [batch]
        v4  = torch.nn.functional.linear(v1, v2) 
        return v4, v4


# Initializing the model