
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v3 = torch.bmm(v1, x2)  # or torch.matmul(v1,x2), both of which will be used for the BMM operation.
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(500, 64, 7) # 500 is the batch size, 64 is the number of input channels and 7 is the height.
x2 = torch.randn(500, 8, 7) # 500 is the batch size, 8 is the number of input channels (in this case it's also equal to 64), and 7 is the height.

