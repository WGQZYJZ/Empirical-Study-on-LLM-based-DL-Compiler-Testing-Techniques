

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.zeros(*v1.shape).to(device='cuda')
        v3  = torch.where(v1 > 0 , v1, v2) # This line can be replaced with v3 = F.leaky_relu(v1), but this line is intentionally written to emphasize the difference between `torch.where` and `torch.nn.functional`.
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(4, 6).to(device='cuda')
 
 