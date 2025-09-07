
class Model(torch.nn.Module):
    def __init__(self, k0 = 528139477):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.k0 = torch.tensor(
            k0, dtype=torch.int64)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = v1 + self.k0 
        return v2


# Initializing the model
m  = Model() 

# Inputs to the model
x1  = torch.randn(378456, 3, 64, 64) 
k0_value = 795370352
