
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5)  # Apply dropout to the input tensor with probability of each element being set to zero is equal to `p`
        v2 = torch.rand_like(v1)
        return v2


# Initializing and generating inputs for the model
m = Model()
x1 = torch.randn(3, 4)
