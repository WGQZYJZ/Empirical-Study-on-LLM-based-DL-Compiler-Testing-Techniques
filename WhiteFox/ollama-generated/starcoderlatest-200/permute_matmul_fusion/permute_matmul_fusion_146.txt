
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1).contiguous() # or v1 = x1.view(-1, 2, 1).permute(0, 2, 1).contiguous() for Torchscript
        t2 = x2.permute(0, 2, 1).contiguous()
        v3 = torch.bmm(t1, t2) # or v3 = torch.matmul(t1, t2)
        return self.linear(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 5, 2)
