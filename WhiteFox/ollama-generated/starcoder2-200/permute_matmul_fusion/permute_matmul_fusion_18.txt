
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
         v1  = x1.permute([0, 2, 1])
         v3  = torch.bmm(v1, self.linear.weight)[..., None] + self.linear.bias[..., None]
         return v3

# Initializing the model