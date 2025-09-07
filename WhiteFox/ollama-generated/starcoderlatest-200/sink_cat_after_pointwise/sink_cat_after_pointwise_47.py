
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1)
        v2 = v1.view(-1, 4)
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()


## The two input tensors to the model are different but satisfy the requirements of the pattern
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 5)
