
class Model(torch.nn.Module):
    def __init__(self, model_size):
        super().__init__()
        self.conv = torch.nn.Conv2d(model_size, 16, 3, stride=2, padding=1)
 
    def forward(self, x1, mask):
        output = F.normalize(self.conv(x1), p=2, dim=-1)
        output = output * (mask * 0.7071067811865476)
        return output


# Initializing the model
m = Model()

