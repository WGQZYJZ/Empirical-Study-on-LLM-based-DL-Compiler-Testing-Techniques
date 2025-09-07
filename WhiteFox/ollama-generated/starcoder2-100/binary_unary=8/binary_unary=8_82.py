
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
other_tensor = torch.randn(1, 8, 64, 64) - 0.5 + 1e-7
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

The code in Model.py should generate both models and inputs for the system to run (i.e., when you click on "Run" button after pasting the text above). 
