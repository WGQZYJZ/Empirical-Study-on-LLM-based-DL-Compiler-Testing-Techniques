
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x1[:, i * size:(i + 1) * size] for i in range(0, int(x1.shape[1] / size))], dim=1)
        return v1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 9223372036854775807) # Please input a valid tensor here!
