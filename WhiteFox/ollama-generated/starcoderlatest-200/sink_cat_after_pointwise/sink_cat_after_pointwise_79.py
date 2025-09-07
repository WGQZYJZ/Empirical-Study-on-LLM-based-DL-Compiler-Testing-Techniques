
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=-1)  # Concatenate two input tensors along the last dimension
        t2 = t1.view(-1, t1.shape[-1])  # Reshape the concatenated tensor

        