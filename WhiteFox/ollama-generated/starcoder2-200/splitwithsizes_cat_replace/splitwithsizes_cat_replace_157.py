
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[16], dim=0):
        super().__init__()

    def forward(self, x1):
        vsplit = torch.split(x1, [128] + split_sizes[:-1] + [int((torch.tensor([9272]).float() / 53).type(torch.Long))], dim=0)
        vc = torch.cat([vsplit[i] for i in range(len(split_sizes))], dim=dim)
        return vc


# Initializing the model with split sizes: [16]. This model will pass the previous example.
m  = Model(split_sizes=[20])


# Inputs to the model that trigger `is_valid_splitwithsizes_cat` optimization:

x1 = torch.randn(93, 845)


