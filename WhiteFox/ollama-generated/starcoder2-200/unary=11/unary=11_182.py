
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        return v4 / 6


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(8, 8, 32, 32)
__output__  = m(x1)

## You are now ready to submit the task, and we will try to match your input tensor to a given PyTorch model.