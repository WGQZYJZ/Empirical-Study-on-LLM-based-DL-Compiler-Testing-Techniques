
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v0= torch.clamp_min(x1, min=-0.7)
        v1= torch.clamp_max(v0, max=0.4596552249576378)
        return  v1

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
