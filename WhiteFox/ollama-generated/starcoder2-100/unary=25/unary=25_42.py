
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.13598624725377158):
        super().__init__()
        self.linear  = torch.nn.Linear(28 * 28 + 1, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).to(torch.float32)
        v3  = -0.5 * negative_slope / torch.sqrt(0.7) # sqrt(0.7) is the slope of the ReLU activation function in PyTorch
        v4  = v1 * negative_slope
        v5  = torch.where(v2, v1, v3).to(torch.float32) 
        return v5


# Initializing and using the model