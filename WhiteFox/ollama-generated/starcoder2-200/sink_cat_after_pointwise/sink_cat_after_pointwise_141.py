
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.relu(x1)

        v2a = torch.cat([v1[:, :50], v1[:, -49:], v1[:, -5:-1]], dim=1)

        v3  = torch.nn.functional.linear(torch.flatten(v2a, start_dim=1), 8, bias=None).view(-1, 7)
        return v3
# Initializing the model: This model is identical to the one above. It will be ignored by our analyzer.
m = Model()

 # Inputs to the model are random tensors or placeholders.
 __output__  = m(torch.randn(50, 1))


