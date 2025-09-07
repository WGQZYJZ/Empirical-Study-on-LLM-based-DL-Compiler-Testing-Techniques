
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        v3  = F.relu(v2) # Replace other with a scalar for F.relu to match this pattern; replace the "other" with the scalar in the final output for this pattern
        return v3

# Initializing the model
m  = Model()

