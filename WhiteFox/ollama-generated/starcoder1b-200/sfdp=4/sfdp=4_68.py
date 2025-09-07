
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        query_mask = torch.ones(x1.size())  # Use identity matrix for the query
        key = torch.randn((query_mask.size(-1), 256))  # Generate random keys
        attn = torch.bmm(query_mask, value)  # Compute dot product of the query and value
        output = torch.bmm(attn_weights * query, value)  # Compute weighted sum of the value tensors

    def extra_repr(self):
        s = super().extra_repr() + "\n"
        return s


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
