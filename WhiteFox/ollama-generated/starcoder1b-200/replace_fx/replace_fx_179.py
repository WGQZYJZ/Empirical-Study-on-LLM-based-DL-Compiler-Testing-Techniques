
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Original nodes in the graph.
        self.old_dropout1 = torch.nn.functional.dropout(x1, 0.5)
        self.old_randlike1 = torch.rand_like(x1)

        v1 = x1.permute(0, 2, 1)
        # The `fallback_random` configuration parameter in the model will turn on this.
        if self.training and self.device.type == 'cuda':
            return (self.old_dropout1 * v1).sum(-1)
        else:
            return (self.old_randlike1 * v1).sum(-1)


# Initializing the model
m = Model()


