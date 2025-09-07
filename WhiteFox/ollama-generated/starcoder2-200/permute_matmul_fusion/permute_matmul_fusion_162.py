
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):

        # First part of model
        v1  = x1.permute(0, 2, 1).contiguous()
        v3  = torch.bmm(v1, self.linear1.weight)

        # Second part of model
        v2  = x2.permute(0, 2, 1)
        v4  = self.linear2(v2)

        # Combining results
        v5  = torch.cat((v3, v4), dim=1).contiguous()

        return v5

# Initializing the model
m  = Model()

