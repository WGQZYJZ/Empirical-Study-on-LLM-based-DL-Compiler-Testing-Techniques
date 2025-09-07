
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        return v1 - other

    def __repr__(self):
        output_type = 'torch.nn.' + str(super().__class__.__name__) + '(' \
            if torch.nn._modules[super().__class__.__name__].__repr__ else super().__class__.__name__)
        repr_string = output_type + '(\n' + str(self.conv) + '\n)'
        return repr_string


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
