
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [16, 16], dim=-1)
        concatenated_tensor = torch.cat([
            split_tensors[i] for i in range(2)], dim=-1)
        return concatenated_tensor


# Inputs to the model
x1 = torch.randn(4, 3, 256, 256)
