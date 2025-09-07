
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 0.5).div(0.7071067811865476)  # Scale the input to a value between -1 and 1. Note that x1.shape = torch.Size([1, 3, 64, 64])
        v3 = torch.nn.functional.dropout(v2, p=0.5)  # Apply dropout on the output of step-3
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
