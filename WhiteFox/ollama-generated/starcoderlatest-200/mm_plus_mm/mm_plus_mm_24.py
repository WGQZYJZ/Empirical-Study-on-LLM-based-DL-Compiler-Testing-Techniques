
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.mm(input1, input2)  # Matrix multiplication between input1 and input2
 
    def forward(self):
        v1 = t1 + self.t1  # Addition of the results of two matrix multiplications
        return v1


# Initializing the model
m = Model()
# Inputs to the model
input1 = torch.randn(1, 3)
input2 = torch.randn(1, 5)
input3 = torch.randn(1, 8)
input4 = torch.randn(1, 9)
