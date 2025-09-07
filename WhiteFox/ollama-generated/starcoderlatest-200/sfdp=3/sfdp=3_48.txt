
class TransformerModel(torch.nn.Module):
    def __init__(self, num_heads: int = 2, dim: int = 64, dropout_p: float = 0.5) -> None:
        super().__init__()
        self.layer1 = torch.nn.Linear(in_features=dim, out_features=dim, bias=True)
        self.layer2 = torch.nn.Linear(in_features=dim * (4 + num_heads), out_features=dim, bias=True)
        self.layer3 = torch.nn.Dropout(p=dropout_p)

    def forward(self, x1, x2):
        v  = torch.cat((x1, x2), dim=-1)  # Concatenate the first and second inputs
        a1 = F.gelu(self.layer1(v))  # Apply gated linear units to the concatenated output
        a2 = self.layer2(a1)  # Apply one more Linear layer followed by an activation function to produce the intermediate tensor
        a3 = self.layer3(a2)  # Apply dropout to the intermedate output
        return a3


# Initializing the model
m = TransformerModel()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 3, 64, 64)
