
class Model(torch.nn.Module):
    def __init__(self, input_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other  = torch.randn(10, requires_grad=True)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        other = self.other.to(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m  = Model()

