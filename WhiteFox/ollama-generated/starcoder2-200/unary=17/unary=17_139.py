
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.relu(v1)
        return v2


# Initializing the model and its inputs to the model.
m  = Model()
 
x1  = torch.randn(1, 3, 64, 64)
 
# Forwarding `m` with the input.
__output__  = m(x1)
 
