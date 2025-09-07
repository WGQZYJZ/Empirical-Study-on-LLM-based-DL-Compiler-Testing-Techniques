
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=0)
        v3 = torch.clamp_max(v2, max_value=1)
        return v3


# Generating an input tensor
x1 = torch.randn(1, 3, 64, 64)

# Running the model to generate output tensors
with torch.no_grad():
    y1 = m(x1)
    print("Output 1: ", y1)
    
