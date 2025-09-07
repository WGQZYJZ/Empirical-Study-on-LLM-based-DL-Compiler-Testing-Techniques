
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        attention_weights = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.shape[0])
        return self.conv(attention_weights.matmul(x2)).contiguous()


# Initializing the model
m = Model()

