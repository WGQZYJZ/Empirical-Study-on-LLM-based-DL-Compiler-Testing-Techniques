
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.input_tensor = inp
 
    def forward(self, x1):
        return self.input_tensor * self.input_tensor + x1 + 1  # Add the result of the matrix multiplication to another tensor 'inp'


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 5, 64, 64)
