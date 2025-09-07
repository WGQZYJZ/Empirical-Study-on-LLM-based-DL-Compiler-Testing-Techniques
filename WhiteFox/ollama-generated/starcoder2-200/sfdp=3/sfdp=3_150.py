
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(3, 4)
 
    def forward(self, x1, x2):
        v1  = self.qk(x1)
        v2  = self.qk(x2)
        v3  = v1 * v2
        return v3


# Initializing the model
m = Model()
__output_one__ = m(torch.randn(4, 5), torch.randn(6, 7))
__output_two__ = m(torch.randn(4, 9), torch.randn(12, 3))

