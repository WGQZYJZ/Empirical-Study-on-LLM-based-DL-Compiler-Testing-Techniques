
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()

        self.layer  = torch.nn.Linear(2, 2)
        self.out_fc = torch.nn.Linear(2, num_classes)

    def forward(self, x1):
        v1  = self.layer(x1)
        v2  = torch.relu(v1)

        return self.out_fc(v2)


# Initializing the model
m = Model()


