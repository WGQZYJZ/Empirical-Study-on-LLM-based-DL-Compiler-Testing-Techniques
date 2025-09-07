
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + torch.randn(v1.size()).to(x1.device).requires_grad_() # Passing the "other" tensor to the addition operation 
        return v2

# Initializing the model
m  = Model()

