

class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()

        self.query  = torch.nn.Parameter(torch.randn(256))
        self.key    = torch.nn.Parameter(torch.randn(256))

    def forward(self, value):
        vq1  = query @ key[::-1] / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        print(vq1)
        vq3   = vq1 * 0.7071067811865476 
        vq4   = torch.erf(vq3)
        vq5  = vq2 + 1 # Add 1 to the output of the error function

        return vq4

# Initializing the model and setting up the required parameters