
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
 
    def forward(self, x):
        split_tensors = torch.split(x, [10, 5], dim=-1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(2)], dim=0)
        return concatenated_tensor


# Initializing the model
m = Model()


