
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.transpose(x1, 1, 0)
        v2 = torch.transpose(x2, 1, 0)
        v3 = torch.bmm(v1, v2)

        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 16, 48, 5) # (B, C_in, H_in, W_in)
x2 = torch.randn(2, 10, 16, 5) # (B, C_out, H_in, W_in)
