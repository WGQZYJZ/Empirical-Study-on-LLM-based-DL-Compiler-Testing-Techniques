
class Model(torch.nn.Module):
    def __init__(self, max_=10., min_=5.):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64**2, 3)

    def forward(self, x1):
        v1 = self.linear(x1.reshape(-1))
        v2 = torch.clamp_min(v1, min_=5.) # Applying torch.clamp_min to the output of the linear transformation with a minimum value set to 5.
        v3 = torch.clamp_max(v2, max_=10) # Applying torch.clamp_max to the previous result with a maximum value set to 10.
        return v3


# Initializing the model
m = Model()
