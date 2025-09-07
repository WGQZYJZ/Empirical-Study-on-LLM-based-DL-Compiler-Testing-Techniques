
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
         return torch.nn.functional.batch_norm(torch.nn.functional.conv2d(input1))

# Initializing the model
m = Model()

# Inputs to the model
input1  = torch.randn(30, 30)

