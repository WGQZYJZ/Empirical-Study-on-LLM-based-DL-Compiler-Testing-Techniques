
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(in_features=768, out_features=4096)
        self.linear2 = torch.nn.Linear(in_features=4096, out_features=256)
        self.dropout = torch.nn.Dropout(p=dropout_p)

    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = torch.relu(v1)
        v3  = self.linear2(v2)
        v4  = torch.relu(v3)
        return self.dropout(v4)

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 768)
