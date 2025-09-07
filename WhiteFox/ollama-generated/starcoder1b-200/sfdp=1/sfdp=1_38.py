
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x) * 0.5
        v2 = torch.softmax(self.conv2(v1), dim=-1) * 0.7071067811865476
        return torch.nn.functional.dropout(v2, p=dropout_p)


# Initializing the model
m = Model()


