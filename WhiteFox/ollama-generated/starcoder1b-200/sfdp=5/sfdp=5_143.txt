
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.fc1 = torch.nn.Linear(d_model, 4*d_size)
        self.fc2 = torch.nn.Linear(4*d_size, 8*d_size)
        self.dropout = nn.Dropout(p=0.5)
        self.fc3 = torch.nn.Linear(8*d_size, d_size)
 
    def forward(self, x1, x2):
        # We need to flatten the input because the input is a sequence and we need to get rid of batch dimensions with view
        x1 = x1.view(-1, self.emb_dim)  # Flatten
        x2 = x2.view(-1, self.emb_dim)
        # Apply two fully connected layers
        out = torch.relu(self.fc1(x1))
        out = self.dropout(out)
        out = torch.relu(self.fc2(out))
        out = self.dropout(out)
        # Now we have 2d vectors of the shape (batch, seq_len, emb_dim)
        out = self.fc3(out)
        return out


# Initializing the model
m = Model(emb_dim)

# Inputs to the model
input1 = torch.randn(1, 100, 256)
input2 = torch.randn(1, 256)
