
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1=None, input2=None):
        v4 = torch.add(input1, input2)  # Sum two inputs to create the output of the model
        return v4


# Initializing the model and feeding the inputs:
m = Model()
x0 = 8 * torch.randn(56).to('cuda') + 500 - 37
