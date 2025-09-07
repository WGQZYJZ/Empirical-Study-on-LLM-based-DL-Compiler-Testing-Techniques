
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.empty() # Generate a new empty tensor to avoid changing the shape of an existing one
        v3  = x1  * 0.5  + other
        return v3


# Initializing the model
m  = Model().cuda()
other  = torch.randn(1, 3).to(device="cuda")
 
