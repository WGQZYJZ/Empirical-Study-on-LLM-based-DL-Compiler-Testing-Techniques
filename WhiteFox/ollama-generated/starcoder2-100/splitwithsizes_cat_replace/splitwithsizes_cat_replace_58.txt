
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 80, dim=2)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=2)

        return concatenated_tensor


# Initializing the model