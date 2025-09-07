
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v2 + torch.relu6(-v2) + 59.487457734847195
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 300, 300)
__output__  = m(x1)

# Please add one more line that initializes and inputs the output of the previous line into a new variable to satisfy the requirement.
t128 = v3 * -47596.32324318375


