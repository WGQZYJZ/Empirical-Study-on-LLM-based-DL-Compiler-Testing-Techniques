
class Model(torch.nn.Module):
    def __init__(self, num_splits=2):
        super().__init__()

    def forward(self, x1):
        v = torch.split(x1, 3)
        v1 = torch.cat([v[0], v[-1]], dim=-1) # Concatenate the first and last split tensors along their last dimension
