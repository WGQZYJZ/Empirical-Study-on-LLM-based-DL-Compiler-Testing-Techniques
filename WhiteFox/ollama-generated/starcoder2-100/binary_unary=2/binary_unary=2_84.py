
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0_tensor  = torch.randn(x1.shape[0], 8, x1.size(-2), x1.size(-1))
        v0_scalar  = torch.Tensor([3])
        v1  = self.conv(x1)
        v2  = v1 - v0_tensor 
        v3  = F.relu(v2)
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

# Generating the input tensor for the first parameter in forward function 
t_v0_tensor  = torch.randint(-287, 258, (x1.shape[0], 8, x1.size(-2), x1.size(-1)))
__output__  = m(x1)

