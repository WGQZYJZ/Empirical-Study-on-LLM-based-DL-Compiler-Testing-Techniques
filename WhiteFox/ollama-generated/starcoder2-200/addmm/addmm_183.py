
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2) # Perform matrix multiplication on two input tensors
        t2  = t1 + inp
        return t2


# Initializing the model
m  = Model()


# Inputs to the model
inp = torch.randn(3,4).to(device="cuda")
x1 = torch.randn(3,4) # Initialize input tensors of sizes (3,4), (3,5) and (7,8).
x2  = torch.randn(3,5)

