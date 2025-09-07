
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        scale = 0.7071067811865475 * torch.sqrt(x1.size()[2] / x1.size()[3])
        v2 = torch.softmax((v1 * scale).contiguous(), dim=-1) # Convert from logits to softmax values
        v3 = torch.matmul(v2, v1)  # Compute scaled dot product
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
