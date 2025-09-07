
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1) 
        v2   = v1 + self.conv(other_tensor) # Adding to the conv
        v3   = torch.relu(v2)  # Applying ReLU 
        return v3


# Initializing the model
m  = Model()


# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64)
other_tensor = torch.randn(8, 3, 62, 62) # different tensor
__output__  = m(x1, other_tensor)

