
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = torch.nn.Linear(784, 1024)
        self.layer_2 = torch.nn.Linear(1024, 256)
        self.dropout = torch.nn.Dropout(p=0.3)

    def forward(self, x):
        x = F.relu(self.layer_1(x))
        x = self.dropout(x)

        x = F.relu(self.layer_2(x))
        x = self.dropout(x)

        return F.log_softmax(self.layer_2(x), dim=1)


# Initializing the model
m  = Model()


