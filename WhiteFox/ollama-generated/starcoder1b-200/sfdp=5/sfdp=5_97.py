
class Model(torch.nn.Module):
    def __init__(self, num_head, dim, dropout_p):
        super().__init__()
        self.fc1 = torch.nn.Linear(dim, dim)
        self.fc2 = torch.nn.Linear(dim, dim)
        self.dropout = nn.Dropout(dropout_p)
 
    def forward(self, x1):
        q = torch.softmax(self.fc1(x1), dim=-1)  # Compute the query using a linear layer with a sigmoid activation function
        k = torch.softmax(self.fc2(x1), dim=-1)  # Compute the key using a linear layer with a sigmoid activation function
        x = q @ k.transpose(-2, -1)  # Compute the dot product of the query and the key, then scale it
        x = self.dropout(x)
        return torch.softmax(self.fc3(x), dim=-1)


# Initializing the model
m = Model(num_head=8, dim=2048, dropout_p=0.5)


