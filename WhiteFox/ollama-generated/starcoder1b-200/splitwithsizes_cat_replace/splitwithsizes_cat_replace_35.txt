
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = torch.tensor([64, 256], dtype=torch.long)
        concatenated_tensors = torch.split(x1, split_sizes, dim=0)
        concatenated_tensor = torch.cat(concatenated_tensors, dim=0)
        return True


# Initializing the model
m = Model()

