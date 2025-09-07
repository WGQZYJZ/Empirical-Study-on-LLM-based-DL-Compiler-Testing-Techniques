
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.ops.aten.mm

    def forward(self, inp=None):  # Pass 'inp' as a keyword argument to the 'forward' function
        v1 = self.mm(input_tensor1, input_tensor2) + inp
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4096)
x2 = torch.randn(4096, 7583)
inp = torch.randn(4096, 7583) # 'inp' is passed as a keyword argument

