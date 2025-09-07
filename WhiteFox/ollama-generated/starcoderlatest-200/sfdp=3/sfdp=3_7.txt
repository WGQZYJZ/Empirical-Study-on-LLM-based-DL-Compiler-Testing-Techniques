
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(768, 1024)
        self.dropout_layer = torch.nn.Dropout(p=dropout_p)
        self.linear = torch.nn.Linear(1024, 128)
 
    def forward(self, x):
        v = self.fc(x)
        v = self.dropout_layer(v)
        v = self.linear(v)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(16, 768)
