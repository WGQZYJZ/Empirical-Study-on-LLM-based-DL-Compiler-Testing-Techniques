
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.Tensor([[-3], [5]])
        self.input2 = torch.Tensor([[-10], [-8]])
 
    def forward(self, inp=None):
        v1 = torch.mm(self.input1, self.input2)  # Perform matrix multiplication on two input tensors
        return v1 + inp


# Initializing the model
m = Model()


# Inputs to the model
inp = torch.randn(2)  # inputs for the model
