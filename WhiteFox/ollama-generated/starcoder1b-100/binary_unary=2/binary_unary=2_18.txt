
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) - torch.zeros(1, 8, 64, 64).to(device=x1.device, dtype=x1.dtype, requires_grad=True)
        return relu(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.zeros(1, 8, 64, 64).to(device=x1.device, dtype=x1.dtype, requires_grad=True)
