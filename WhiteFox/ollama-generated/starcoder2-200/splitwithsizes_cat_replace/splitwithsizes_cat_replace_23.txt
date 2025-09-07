
class Model(torch.nn.Module):
    def __init__(self, splitsize1, splitsize2, dim):
        super().__init__()
 
        self.split = torch.split  # Get a reference to `torch.split` so that we can patch it

        self.conv3x3_1 = torch.nn.Conv2d(
            3,
            splitsize1 + sum(splitsize1),
            3,
            1,
            padding=1
        )

        self.conv7x7_2  = torch.nn.Conv2d(
            80,
            sum(splitsize1) * sum(splitsize2) / splitsize2[dim] , # <-- this line is a potential bug
            3, 1,
            padding=1
        )

    def forward(self, x):

        v1 = self.conv7x7_2(x)
        v1 = torch.split(v1, [int(s * s / len(splitsize2)) for s in splitsize2], dim)[dim]  # <-- this line is a potential bug
        # Concatenate the tensors
        v3  = torch.cat([t.unsqueeze(0) for t in v1], 0).sum(0) # <-- this line is a potential bug

        return v3

# Initializing the model
m  = Model(splitsize=[4,8],[256])

