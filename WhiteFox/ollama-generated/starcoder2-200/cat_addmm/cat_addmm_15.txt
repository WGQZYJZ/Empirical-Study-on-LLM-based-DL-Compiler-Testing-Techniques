
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.fc = torch.nn.Linear(4*4*8, 6)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v1  = v1.view(-1, 4 * 4 * 8)
 
        v2  = self.fc(v1)

        return torch.nn.functional.softmax(v2), v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
__output__ ,__hidden_state__= m(x1)