
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        output  = torch.nn.functional.batch_norm(x1)
        return output

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(2, 320)

# Expected model output
expected_output  = m(x1)

