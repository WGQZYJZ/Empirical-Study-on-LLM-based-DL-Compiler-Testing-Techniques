
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x).permute(-1, -2, 3, 4)


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(8, 9, 6) # Shape [N_batch, N_channel, N_depth]
__output__  = m(x)        # Shape [N_batch, 3*N_channel + 5, N_depth - 2, N_depth]
