
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.nn.Linear(10, 2) # 2 inputs to the model
        self.input2 = torch.nn.Linear(2, 3) # 2 inputs to the model
 
    def forward(self, x1, x2):
        v1 = self.input1(x1)
        v2 = self.input2(x2)
        v3 = t1 + t2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 10) # Batch 1 with length 2
x2  = torch.randn(1, 2)  # Batch 1 with length 3
__output__  = m(x1, x2)


