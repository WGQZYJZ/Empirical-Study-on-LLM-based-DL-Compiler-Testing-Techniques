
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.qk = torch.nn.Linear(8, 16)
 
    def forward(self, x0):
        v0 = self.qk(x0)
        return v0


# Initializing the model
m  = Model()

# Inputs to the model
x0 = torch.randn(256, 49152).float().cuda() # Assuming the input tensor is a randomly generated float32 tensor with the shape [N, L]. Replace [N] and [L] accordingly.
__output__  = m(x0)

