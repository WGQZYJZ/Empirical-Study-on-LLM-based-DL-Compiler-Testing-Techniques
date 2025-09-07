
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other_tensor 
        v3  = relu(v2) # The ReLU function is not used in the pattern example above. Use it as you want. 
        return v3

# Initializing the model
m = Model()

