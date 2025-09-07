
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, x2) / math.sqrt(2 * math.pi)  # Compute the scaled dot product of the input tensors
        v3 = v2.softmax(dim=-1)    # Apply softmax to compute attention weights
        v4 = torch.matmul(v3, x1)   # Compute the weighted sum of the value tensor with attention weights
        return v4


# Initializing the model
m = Model()


