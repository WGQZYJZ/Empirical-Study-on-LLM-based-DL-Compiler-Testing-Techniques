

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 - 5 # Substracting the scalar `5` from `v1`
        v3   = torch.relu(v2) # Applying ReLU activation function to result of subtraction (the output is negative so it should be a zero tensor).
        return v3

# Initializing model
m  = Model2()
x1  = torch.randn(1, 3, 64, 64)

__output__  = m(x1)

