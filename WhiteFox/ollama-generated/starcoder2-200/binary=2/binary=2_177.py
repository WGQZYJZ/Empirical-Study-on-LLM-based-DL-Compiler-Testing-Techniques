
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other # 'other' could be another tensor or a scalar.
        return v2


# Initializing the model and passing a random input tensor 
m = Model()
x1 = torch.randn(1, 3, 64, 64)
v1_input = m(x1) # Passing x1 into the model to initialize it.

__output__  = m(v1_input).detach().numpy()

