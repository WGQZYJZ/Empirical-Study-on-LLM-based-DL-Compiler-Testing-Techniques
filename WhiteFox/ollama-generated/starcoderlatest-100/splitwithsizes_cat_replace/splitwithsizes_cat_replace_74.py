
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [120], dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1)  # <<<< The concatenation is wrong here!!!
        return concatenated_tensor


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
