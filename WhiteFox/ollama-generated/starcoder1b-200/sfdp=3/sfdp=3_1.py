
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = nn.Linear(3, 8)
        self.layer_2 = nn.Linear(8, 4)
        self.layer_3 = nn.Linear(4, 1)
 
    def forward(self, x1):
        x = F.relu(self.layer_1(x1))
        x = F.dropout(x, p=0.25, training=training)
        x = F.relu(self.layer_2(x))
        x = F.dropout(x, p=0.25, training=training)
        x = self.layer_3(x)
        return x


# Initializing the model
m = Model()


