
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_sizes = [2] * 5
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes, dim) for _ in range(4)], dim)
        return concatenated_tensor


# Initializing the model
m = Model()
m.eval()
