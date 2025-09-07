
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2)
        v2  = [v1 for _ in range(len(input1))] # Initialize list to store the output of each element of v1, and then use it as the input of next element in `torch.cat`
        return torch.cat(v2)


# Initializing the model
m  = Model()
x1  = torch.randn(3, 4, 64, 64)
x2  = torch.randn(3, 3)
