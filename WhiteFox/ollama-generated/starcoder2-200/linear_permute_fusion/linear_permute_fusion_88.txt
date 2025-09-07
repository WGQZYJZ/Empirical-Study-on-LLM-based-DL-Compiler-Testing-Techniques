

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)  # Linear function on input tensor.
        return v1.permute(0, 2, 1)


# Initializing the model
m = Model()
__input__  = torch.randn(4, 3, 2)

# Outputs of the model
__output__  = m(__input__)

