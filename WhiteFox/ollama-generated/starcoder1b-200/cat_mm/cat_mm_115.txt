
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        t1  = torch.mm(input1, input2)
        t2 = torch.cat([t1, t1, ..., t1], dim=-1)  # Concatenation along the specified dimension
        return t2


# Inputs to the model
input1 = torch.randn(10, 3, 4)  # Input tensor for a matrix multiplication operation
input2 = torch.randn(10, 3, 5)  # Input tensor for another matrix multiplication operation
