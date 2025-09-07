
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4, 8)
        self.conv = torch.nn.Conv2d(8, 4, 3, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.relu(self.linear1(x1))
        v2 = self.conv(v1)
        output = torch.matmul(v2, x2)
        return output


# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(1, 4, 64, 64) # Query
x2 = torch.randn(3, 4, 64, 64) # Key
