
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Input tensor to the model
        t1 = torch.mm(x1, x2) 
        t2 = torch.cat([t1] * self._concat_axis_length, dim=0)
        return t2

# Initializing the model
x1 = torch.randn(3, 4)  # Input tensor to the matrix multiplication operation in the model; shape: [3, 4]
x2 = torch.randn(5, 6)  # Input tensor to the matrix multiplication operation in the model; shape: [5, 6]

model = Model()
model._concat_axis_length = 10000
