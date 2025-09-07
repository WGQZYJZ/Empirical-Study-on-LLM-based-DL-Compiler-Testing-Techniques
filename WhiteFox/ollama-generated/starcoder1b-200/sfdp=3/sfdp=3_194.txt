
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=0)
 
    def forward(self, x):
        w1 = self.conv1(x)
        w2 = self.conv2(w1)
        v1 = F.softmax(w2, dim=-1)
        v2 = F.dropout(v1, p=0.5, training=self.training)
        w3 = self.conv1(v2)
        w4 = self.conv2(w3)
        return v1 * w4


# Initializing the model
m = Model()

