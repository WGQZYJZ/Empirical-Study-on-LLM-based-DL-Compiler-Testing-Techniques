
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + torch.randn_like(v1) 
        return v2

# Initializing the model with a random number generator seed
m = Model()
torch.random.manual_seed(307845964)  # You may use any number that satisfies the requirements

