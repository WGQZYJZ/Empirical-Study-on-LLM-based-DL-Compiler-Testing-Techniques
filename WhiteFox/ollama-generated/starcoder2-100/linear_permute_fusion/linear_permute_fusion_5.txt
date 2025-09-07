
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Linear transformation applied to the input tensor x1
        v2 = v1.permute(0, 3, 1, 2).contiguous()  # Permute the output of linear function on v1
        return v2

# Initializing the model
m = Model()

# Inputs for the model
x1 = torch.randn(4, 2)

# Output from the model
