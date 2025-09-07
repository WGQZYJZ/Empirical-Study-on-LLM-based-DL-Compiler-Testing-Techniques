
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)
        return v3


# Initializing the model with an initial value for `other_tensor`
m  = Model()
m(input_tensor)
 
other_tensor = torch.randn(()) # Initialize another tensor
 
# Initializing a second model, whose inputs will be different from those of the first one
m2  = Model()
m2(second_input)

