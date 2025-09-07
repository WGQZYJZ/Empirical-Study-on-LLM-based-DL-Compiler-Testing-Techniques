
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.concat = torch.cat([
            torch.randn((3200)), 
            torch.zeros((size, 9))
        ], dim=1)
 
        self.slice1 = self.concat[:, :3] 
        self.slice2 = self.slice1[:size,:]
        self.concat2 = torch.cat([self.concat, self.slice2], dim=1)
 
    def forward(self, x):
        return 0


# Initializing the model
m = Model(500)


# Inputs to the model