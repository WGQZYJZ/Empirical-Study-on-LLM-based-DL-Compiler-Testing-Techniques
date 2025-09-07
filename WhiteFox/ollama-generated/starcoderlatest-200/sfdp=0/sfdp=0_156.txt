
class MultiHeadAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.head = torch.nn.ModuleList([
            torch.nn.Linear(3, 64),
        ])
 
    def forward(self, query, key, value):
        x1 = []
        for l in range(8):
            # Get the linear output of each head layer
            x = self.head[l](torch.cat((query[:, :, l], key[:, :, l]), dim=2))
            x1 += [x]
 
        # Concatenate the different heads' outputs together, and reshape to (batch_size, 16, 108)
        x1 = torch.cat(x1, dim=2).reshape((32, 16, 108))
        