
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Add 3 to the output of the linear transformation
        v3  = F.selu(v2) 
        v4  = v3 /6 # Divide by 6
        return v4
# Initializing the model