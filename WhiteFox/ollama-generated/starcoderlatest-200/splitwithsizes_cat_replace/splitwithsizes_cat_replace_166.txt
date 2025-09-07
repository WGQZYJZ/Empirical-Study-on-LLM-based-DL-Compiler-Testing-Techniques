
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.split(x1, split_sizes=[32], dim=1)
        v2 = torch.cat([v1[i] for i in range(len(split_sizes))], dim=1) # Trigger is_valid_splitwithsizes_cat optimization here!
