
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inp = torch.randn((3, 4), dtype=torch.float64)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp # 3 * 4 matrix * 3 * 4 matrix = 4 * 3 matrix, 4 * 3 matrix + 3 * 4 matrix = 7 * 4 matrix
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5, 9)
x2  = torch.randn(9, 6) # Shape of both tensors is (N, D). N is a constant that is not relevant for this task and will be ignored in your results.
__output__  = m(x1, x2)

