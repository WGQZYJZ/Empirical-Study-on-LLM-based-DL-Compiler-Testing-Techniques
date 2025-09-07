
class Model(torch.nn.Module):
    def __init__(self, input1_size=256, input2_size=2048):
        super().__init__()

    def forward(self, input1, input2):

        v1 = torch.mm(input1, input2)

        v2  = torch.cat([v1]*3)

        return v2

# Initializing the model
m = Model()

 # Inputs to the model
input1 = torch.randn(8, 4096, dtype=torch.float)
input2 = torch.randn(8, 4097, 5, dtype=torch.float)
