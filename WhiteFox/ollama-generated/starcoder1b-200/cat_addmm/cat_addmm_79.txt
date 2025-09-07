
class Model(torch.nn.Module):
    def __init__(self, num_layers, hidden_dim, dropout=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, x1, x2):
        m = torch.addmm(x1, x2, x2)
        # Concatenate the result along a specified dimension
        return torch.cat([torch.relu(m), torch.softmax(m)], dim=1)


# Initializing the model
model = Model(num_layers=3, hidden_dim=4, dropout=0.5)
x1 = torch.randn(1, 4, 8)
x2 = torch.randn(1, 4, 8)
