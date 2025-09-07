
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).to(dtype=torch.bool) # Apply the greater than operator to each element in v1, and convert the resulting boolean mask to a torch.bool tensor using .to(dtype=torch.bool)
        v3  = negative_slope * - v1 # Multiply the negative slope by each element of v1
        v4  = torch.where(v2, v1, v3) # Apply where function on v2 and v3 to select elements from v1 or v3 based on mask v2
        return v4


# Initializing the model