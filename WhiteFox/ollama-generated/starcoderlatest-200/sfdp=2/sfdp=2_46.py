
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(128, 256)
 
    def forward(self, x1):
        qk = self.qk(x1)
        return qk


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att1 = Attention()
 
    def forward(self, x1, x2):
        a1 = self.att1(x2)  # Compute the attention vector for the second input tensor
        output  = torch.matmul(a1, x1)  # Compute the dot product of the attention vector and the first input tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
