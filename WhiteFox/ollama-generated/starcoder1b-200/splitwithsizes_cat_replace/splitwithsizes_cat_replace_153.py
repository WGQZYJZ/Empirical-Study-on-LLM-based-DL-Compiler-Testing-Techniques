
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.split(x1, [64], dim=0)  # Split the input tensor into 2 tensors along the first dimension
        v2 = [torch.cat([v1[i], v1[i]], dim=0) for i in range(len(v1))]  # Concatenate the two split tensors along their corresponding dimensions
        return torch.cat(v2, dim=0)


# Initializing the model
m = Model()
