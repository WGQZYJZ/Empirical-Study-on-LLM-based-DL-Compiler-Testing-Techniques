
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # Applying a clamp operation to the addition of a tensor and a constant
        v4  = torch.clamp_max(v3, 6) # Applying another clamp operation after the first one is applied
        v5  = v4 / 6 # Divide the clamped value by 6
        return v5


# Initializing the model
m1  = Model()
 
# Input to m1
x1_1   = torch.randn(1, 3, 28, 28) 

# Output of m1 after feeding x1 into it 
output__m1 = m1(x1_1)

# Initializing a different model for the next input and output values
m2   = Model()
 
# Input to m2
x1_2  = torch.randn(3, 3, 64, 64)

# Output of m2 after feeding x2 into it 
output__m2 = m2(x1_2)

