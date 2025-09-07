
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cat = torch.nn.Cat((torch.nn.Flatten(),), dim=1)
 
    def forward(self, x1, size):
        v1 = self.cat([x1, x1])
        v2 = v1[:, 0:size]
        return v2
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
size = 9223372036854775807
