
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.cat([x1[:, :], x1[:, 9223372036854775807:]], dim=1)
        v1 = v0[:, :, ::]
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(size=(6, 2)) # The size of x is (batch_size * n_channel, sequence_length)

