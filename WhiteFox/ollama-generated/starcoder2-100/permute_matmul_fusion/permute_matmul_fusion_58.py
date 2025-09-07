
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1, x2): # x1 and x2 should have the same shape
        v1 = torch.bmm(x1, x2.permute(0, 3, 2, 1))  # or torch.matmul(t1, t2)
        return self.linear(v1.reshape(-1, 64))

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 20, 20).to('cuda') # 20 is an arbitrary number for the dimension
x2 = torch.randn(3, 64, 100) # 64 is 8 * 8 = 2^4 * 5 = 1920 * 1/32
