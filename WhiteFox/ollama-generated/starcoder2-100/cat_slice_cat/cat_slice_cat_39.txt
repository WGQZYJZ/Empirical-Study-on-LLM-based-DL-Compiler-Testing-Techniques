
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *inputs):
        v0 = torch.cat(list(inputs), dim=1)
        v3 = v0[:, 0:9223372036854775807]
        v2 = v3[:, 0:-size]
        v1 = torch.cat([v0, v2], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x0 = torch.randn(1, 9223372036854775807 - size + 1) # make sure this is smaller than `size` 
x1 = torch.randn(1, 9223372036854775807 - size + 1) # make sure this is smaller than `size` 
