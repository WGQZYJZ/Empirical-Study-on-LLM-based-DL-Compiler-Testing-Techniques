
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1.clamp_min(-5., max=64.) 
        return v2

# Initializing the model and testing
m  = Model()
torch.manual_seed(0) # Setting seed for reproducibility of test case result
x1  = torch.randn(1, 3, 72, 95)
print(f"The output: {m(x1)}")

