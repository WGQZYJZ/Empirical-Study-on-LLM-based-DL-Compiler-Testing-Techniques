
class Model(torch.nn.Module):
    def __init__(self, dim=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(dim=3, dim=8, kernel_size=1)
 
    def forward(self, x1, x2):
        v  = self.conv(x1).transpose(-2, -1) @ x2 # Use the dot product of the input tensors to compute a weighted sum
        return torch.softmax(v, dim=-1) # Softmax on the result


# Initializing the model
m = Model()

