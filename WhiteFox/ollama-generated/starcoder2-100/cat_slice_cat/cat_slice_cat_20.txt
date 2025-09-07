
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input0, input2):
        v1 = torch.cat([input0, input2], dim=1)[:, 9223372036854775807]
        return torch.stack(torch.split(v1, size), dim=1)

# Initializing the model
m = Model()

# Inputs to the model (the first two inputs are 9223372036854775807)
input0_9223372036854775807, input1_9223372036854775807  = torch.randn(1, 3), torch.randn(1, 3)

# Input size (the third input is 42)
input2_size = 42
