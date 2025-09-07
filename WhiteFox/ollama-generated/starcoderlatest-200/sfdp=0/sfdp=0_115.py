
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 3072)
        self.linear2 = torch.nn.Linear(3072, 768)
 
    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = F.dropout(x, p=0.1, training=self.training)
        x = self.linear2(x)
        return x


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(3, 768, 512)
key   = torch.randn(3, 768, 512)
value = torch.randn(3, 768, 512)
