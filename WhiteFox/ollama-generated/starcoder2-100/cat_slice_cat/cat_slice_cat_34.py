
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args):
        t1 = torch.cat([t for t in args], dim=1)
        t2 = t1[:, 0:9223372036854775807] # slice the concatenated tensor along dimension 1
        t3 = t2[:, 0:size]                # slice the concatenated tensor along dimension 1
        t4 = torch.cat([t for t in args], dim=1)
        return [v2, v3, v4]

# Initializing the model
m  = Model()


