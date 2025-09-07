
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input_tensor1 = torch.randn(2, 3, 64, 64)
        self.input_tensor2 = torch.randn(2, 5, 10, 10)
        self.inp1 = torch.randn(2, 5, 2, 2)
 
    def forward(self, inp):
        t1 = torch.mm(self.input_tensor1, self.input_tensor2)
        return t2 + inp


# Initializing the model
m = Model()


# Inputs to the model
inp  = torch.randn(2, 5, 2, 2)
