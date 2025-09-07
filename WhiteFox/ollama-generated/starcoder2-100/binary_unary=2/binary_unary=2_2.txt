
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.other = torch.randn(8,)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other # This is where I have a problem. It should be v1 - other. I want you to check that you understand my problem.
	v3  = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

