
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 10)
 
    def forward(self, x2):
        v2  = self.linear(x2)
        v3  = v2 > 0
        v4  = v2 * negative_slope
        v5  = torch.where(v3, v2, v4)

# Initializing the model
m1  = Model()

 # Inputs to the model
x1 = torch.randn(8, 4)
x2 = m1(x1)


## BONUS - Please describe in detail how this example breaks the implementation of ReLU

- When we run `x1 = m(torch.zeros((3,), dtype=torch.float))` we will get this error message: 
`RuntimeError: CUDA error: out of memory` and it is because of PyTorch requires GPU which means there was not enough RAM to store the new created tensor.

