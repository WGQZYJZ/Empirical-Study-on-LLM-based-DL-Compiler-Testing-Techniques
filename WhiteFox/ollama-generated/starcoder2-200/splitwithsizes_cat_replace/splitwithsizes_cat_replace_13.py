
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[16], dim=0):
        super().__init__()

    def forward(self, x1):
        splitted = torch.split(x1, split_sizes, 3) 
        out = torch.cat([splitted[i] for i in range(len(split_sizes))], 3)
        return out


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 480, 272, 96)
