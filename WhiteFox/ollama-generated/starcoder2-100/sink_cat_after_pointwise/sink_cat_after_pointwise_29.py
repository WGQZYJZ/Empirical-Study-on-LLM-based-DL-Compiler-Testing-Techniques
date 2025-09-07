
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1 = torch.cat([x1 + 1, y1], dim=2)
        v2 = v1.view(-1, 3 * 4096)
        v3 = torch.nn.functional.relu(v2)  # Apply ReLU
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(5, 3, 3 * 4096 + 1).to('cuda')
y1 = torch.randn(5, 2, 3* 4096)
__output__  = m(x1, y1)

