
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v1  = torch.stack([x1 for _ in range(3)]).permute(0, 1)
        v2  = torch.stack([y2 for _ in range(4)]).permute(0, 1) # stack_like: [v1.size() for _ in range(4)]
        v3 = torch.bmm(v1, v2)
        return v3

# Initializing the model
m  = Model()


