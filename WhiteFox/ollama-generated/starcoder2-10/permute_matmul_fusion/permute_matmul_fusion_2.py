
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
         t1  = x1.permute(0, 2, 1)
         t2  = torch.bmm(t1, x2) # or torch.matmul(t1, x2)
         return t2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(30, 64, 5)
x2 = torch.randn(30, 5, 8) # or torch.randn(30, 8, 5)

 