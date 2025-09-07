
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1 = torch.cat([x1 + 2., y1], dim=0)
        v2 = v1.view(-1, 3)
        v3 = torch.nn.functional.relu(v2 - 4.)
        return v3
# Initializing the model<|end_of_model|>m = Model()<|end_of_init|>

