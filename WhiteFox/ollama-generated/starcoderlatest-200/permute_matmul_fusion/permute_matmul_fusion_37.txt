
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        t1 = x1.permute(...) # Permute the input tensor A
        t2 = x2.permute(...) # Permute the input tensor B
        t3 = torch.bmm(t1, t2) # or torch.matmul(t1, t2)
        return self.linear(t3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
