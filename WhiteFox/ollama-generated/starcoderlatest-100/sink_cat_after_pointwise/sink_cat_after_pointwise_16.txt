
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2, x3], dim=0)
        t2 = t1.view(2, -1).unsqueeze(dim=-1) # [2, 6] tensor of shape (n, c_in, 1) is reshaped to [(n*c_in)] tensor of shape (n*c_in,) with one element as a length and another elements in each dimension.
        t3 = torch.relu(t2) # Pointwise ReLU is applied on the [n*c_in] tensor of shape (n*c_in,) by invoking relu function at that input.
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2) # Shape (4, 2)
x2 = torch.randn(4, 2) # Shape (4, 2)
x3 = torch.randn(4, 2) # Shape (4, 2)
