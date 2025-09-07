
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.conv.weight)  # input shape [1, N_i, C_i, H_i, W_i]
        v2 = torch.nn.functional.batch_norm(v1, ... , v2 = None)   # output shape [1, N_o, C_o, H_o, W_o]
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(...)
