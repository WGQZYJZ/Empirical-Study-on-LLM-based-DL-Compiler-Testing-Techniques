
class Model(torch.nn.Module):
    def __init__(self, d1 = 4, d2 = 8):
        super().__init__()
        self.fc1 = torch.nn.Linear(d1 * d2 + 30976 // d2 ** 2 - 512, d2)

    def forward(self, x1):

        v1 = x1[:, :d1]
        v4_mask  = self.fc1(v1).exp() > .8  # Create a tensor of mask based on an expression

        v3 = v1.masked_scatter_(v4_mask, -2.) + 5
        v6 = torch.cat([x1[:, d1:], x1[None].repeat((v3.shape[-1], 1, 1)) * v3[:, None]], dim=0)

        return v6

# Initializing the model and assigning the values for dimensions of the tensor
d1_range = torch.arange(48, 72 + 1) # Generate a list from d1=48 to d1 = 72 inclusive
d2_range = torch.arange(609536 // d1_range[None] ** 2 - 512 + 1).type(torch.int64)[::128][:4] # Generate a list of d2 values starting at 0, and then take every 128th element in the list

m = Model()

