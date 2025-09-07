
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).to(torch.float32) * (-0.5) + ((v1 <= 0).to(torch.float32)) * torch.tensor(-0.99, requires_grad=True, device='cuda') # Create a mask based on whether the value is greater than zero
        v3 = torch.where(v2 > 0, (v1 * (-0.5) + ((v1 <= 0).to(torch.float32)) * -0.99).to(x1), v1) # Select values based on mask 
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
