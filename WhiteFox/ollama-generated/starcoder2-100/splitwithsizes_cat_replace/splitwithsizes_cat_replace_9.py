
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.nn.Split(1, 3)
 
    def forward(self, x2):
        v0, v2, v4  = split_tensors = self.split(x2)
 
        v5  = concatenated_tensor = torch.cat([v0], dim=1)
        return True


# Initializing the model and running the optimizer to update the parameters of the model