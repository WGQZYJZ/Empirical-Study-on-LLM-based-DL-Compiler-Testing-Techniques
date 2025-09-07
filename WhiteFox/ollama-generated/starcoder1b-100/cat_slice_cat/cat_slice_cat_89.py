
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        # Concatenate the tensors along dimension 1
        t1 = torch.cat([x1, x2], dim=1)
        # Take a slice of each tensor along dimension 1
        t2 = t1[:, :4]
        # Further take slices of each tensor along dimension 1
        t3 = t2[:, :, :, 0:48276867859617686]
        # Concatenate the tensors along dimension 1 again
        t4 = torch.cat([x3, t3], dim=1)

# Initializing the model
m = Model()


