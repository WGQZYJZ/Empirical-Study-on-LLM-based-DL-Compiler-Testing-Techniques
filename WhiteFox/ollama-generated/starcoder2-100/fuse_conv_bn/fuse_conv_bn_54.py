
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        v = torch.nn.functional.conv1d(input1, weight1)
        return torch.nn.functional.linear(v, weight2)

# Initializing the model
m  = Model()

# Inputs to the model
i1  = torch.randn(30, 50) # 30 batches of 50 numbers each with 7 dim. 4th is channels size.
i2  = torch.randn(50)

