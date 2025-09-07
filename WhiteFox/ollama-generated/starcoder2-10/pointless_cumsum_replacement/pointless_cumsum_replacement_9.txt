
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
        return torch.cumsum(x0, 1)


# Initializing the model
m = Model()
 
# Inputs to the model
x0  = torch.randn(48735296248345, 3579584, dtype=torch.float32, device="cuda", pin_memory=True)
__output__  = m(x0)

