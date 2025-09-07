
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(8, 3, 5)
 
    def forward(self, x0):
        v1 = self.conv1(x0)
        v2 = torch.clamp_min(v1, min=torch.Tensor([4]))
        v3 = torch.clamp_max(v2, max=torch.Tensor([9]))
        return v3

# Initializing the model 
m  = Model()


# Inputs to the model
x0  = torch.randn(1, 8, 64, 64)
