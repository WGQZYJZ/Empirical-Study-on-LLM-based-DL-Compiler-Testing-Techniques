
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v3 = torch.bmm(v1, x2)

        # Permute and concatenate the input tensors B with 2x2 zeros
        v4 = torch.zeros(x2.size(0), 2, 2).to(x2.device)
        v5 = x2 + v4
        v6 = torch.bmm(v1, v5)

        return v3


# Initializing the model
m  = Model()

# Inputs to the model
i1  = torch.randn(2, 20, 2)
i2  = torch.zeros_like(i1, dtype=torch.float64)
