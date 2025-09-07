
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2)
        concat_result = [v1, v1, ..., v1]
        return torch.cat(concat_result, dim=1)


# Initializing the model
m  = Model()
