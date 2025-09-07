
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 5)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor A 
        v3  = x2.permute(0, 2, 1) # Permute the input tensor B

        v4  = torch.bmm(v1, v3).permute(1, 0, 2)
        v5  = torch.nn.functional.linear(v4, self.linear1.weight, self.linear1.bias)

        return torch.nn.functional.linear(v5, self.linear2.weight, self.linear2.bias)

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 4)
x2  = torch.randn(1, 3, 5)

 __output__  = m(x1, x2)


