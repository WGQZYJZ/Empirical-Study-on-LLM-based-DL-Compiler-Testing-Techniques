
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute((0, 2, 1))  # permute tensor A 
        v3 = x2.permute((0, 2, 1))  # permute tensor B

        v4_one = torch.bmm(v1, self.linear)
        v4_two = torch.bmm(self.linear, v3)
        
        return v4_one + v4_two


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1,2,2)
x2  = torch.randn(1,2,2)
__output__  = m(x1, x2)


