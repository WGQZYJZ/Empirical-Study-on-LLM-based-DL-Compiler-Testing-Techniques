
class Model(torch.nn.Module):
    def __init__(self, d1=0., d2=0.):
        super().__init__()
        self.conv = torch.nn.Conv1d(256, 340, kernel_size=(7,))

    def forward(self, t1, t2):
        v1 = torch.cat([t1, t2], dim=-1) # Concatenate tensors along the last dimension.
        v2 = self.conv(v1) # Apply convolution on concatenated tensor.
        return torch.relu(v2)


# Initializing the model