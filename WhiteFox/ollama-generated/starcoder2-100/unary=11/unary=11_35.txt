
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = F.relu6(v2) # In the original version of this model, we directly used torch.clamp_min and torch.clamp_max to clamp the result at a minimum of `0` and maximum of `6`, but we also need to add torch.nn.functional in this test case, which is not mentioned elsewhere in this project.
        v4  = F.hardtanh(v3) # Add torch.nn.functional in this test case
        v5  = v4 / 6
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 7, 9)


__output__  = m(x1)