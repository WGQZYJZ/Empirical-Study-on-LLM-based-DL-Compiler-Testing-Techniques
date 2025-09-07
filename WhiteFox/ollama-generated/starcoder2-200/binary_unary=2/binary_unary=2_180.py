
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        v3  = F.relu(v2)
        return v3


# Initializing the model and input tensor for the model with randomly generated values:
other_tensor  = torch.randn(8, 3, 4, 5) # Randomly generate a 5D tensor of shape (8, 3, 4, 5) that contains random floats between [-1.0, +1.0] for each element in the tensor
m  = Model()


