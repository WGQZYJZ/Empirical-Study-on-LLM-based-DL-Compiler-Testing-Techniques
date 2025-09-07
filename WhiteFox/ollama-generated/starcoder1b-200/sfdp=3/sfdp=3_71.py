
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
        self.linear  = torch.nn.Linear(8 * 5 * 4 * 4, 512)

    def forward(self, x1):
        v1 = self.conv1(x1).view(x1.size(0), -1)
        v2 = self.conv2(v1).view(x1.size(0), -1)
        return torch.cat([torch.nn.functional.softmax(self.linear(v2)),
                            self.linear(torch.nn.functional.dropout(v1, p=dropout_p))], dim=-1)

# Initializing the model
m = Model()


