
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other_tensor
        v3 = F.relu(v2)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

 # In the actual program, there may be more than one place where other tensor is defined and used in different expressions, and it may be unclear which version of "other" the output should be subtracted from
other_tensor = torch.randn(10, 237, 64)
__output__   = m(x1)
