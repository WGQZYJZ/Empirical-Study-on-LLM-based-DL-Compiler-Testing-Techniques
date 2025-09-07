
class Model(torch.nn.Module):
    def __init__(self, n_head=8, depth=16):
        super().__init__()
        self.n_head = n_head
        self.depth = depth
        assert depth % 2 == 0
        for i in range(1, self.depth, 2):
            setattr(self, 'layer' + str(i), Layer(
                n_head=self.n_head//2,
                n_layer=i
            ))

    def forward(self, x, mask=None):
        output = x
        for i in range(1, self.depth, 2):
            layer = getattr(self, 'layer' + str(i))
            output = layer(output, mask=mask)
            output *= math.sqrt(output.size(-1).float())
        return output


# Initializing the model
m = Model()

