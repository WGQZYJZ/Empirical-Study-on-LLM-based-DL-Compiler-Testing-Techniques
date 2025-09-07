
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        # concatenate two tensors along dimension=0 (e.g., dim=0 = tensor1 + tensor2)
        v1 = torch.cat([t1, t2], dim=0)
        v2 = v1.view(-1)
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
t1 = torch.randn(2, 2)
t2 = torch.randn(3, 4)
