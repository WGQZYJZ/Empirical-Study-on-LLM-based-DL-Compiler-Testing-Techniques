
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(2, 4)

    def forward(self, x1): 
        v7 = torch.einsum("abcde,bcde->abde", (x1, x1))
        v8 = self.matmul(v7)

        return v8

# Initializing the model
m = Model()

# Inputs to the model 
x2  = torch.randn(4096, 512*3)
x2  = x2.reshape(32, -1, 512)
__output__  = m(x2)

