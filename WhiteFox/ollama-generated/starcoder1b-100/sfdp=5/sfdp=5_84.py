
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.fc1 = torch.nn.Linear(d_model, 512)
        self.fc2 = torch.nn.Linear(512, d_model)
        self.dropout = torch.nn.Dropout(0.3)
        self.linear = torch.nn.Linear(d_model, 2)
 
    def forward(self, x1):
        v = self.fc1(x1)
        v = F.gelu(v)
        v = self.dropout(v)
        v = self.fc2(v)
        return self.linear(v)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 4096)
x2  = m(x1)


