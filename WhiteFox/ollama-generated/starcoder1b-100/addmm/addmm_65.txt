
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor):
        super().__init__()
        self.inp = inp
 
    def forward(self, x1, x2):
        return self.inp + x1  # Add the result of the matrix multiplication to another tensor 'x1'


# Initializing the model
m = Model(torch.randn(3, 4, 64, 64))


