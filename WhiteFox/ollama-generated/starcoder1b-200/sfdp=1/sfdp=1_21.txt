
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, mask1, mask2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        output = v6
        
        output *= mask1
        output += (mask2 - mask1).to(device=output.device)  # Add the value tensor to the output
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mask1 = torch.ones(1, 10).to(device=output.device)
mask2 = torch.zeros(1, 5).to(device=output.device)
